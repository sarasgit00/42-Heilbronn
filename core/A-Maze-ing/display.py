"""Interactive curses renderer for A-Maze-ing.

Draws the maze, animates the solution path, and handles keyboard
input (arrow-key menu and direct hotkeys R / H / C / Q).
"""

import curses
import time
from typing import Optional

from mazegen.generator import MazeGenerator

NORTH, EAST, SOUTH, WEST = 1, 2, 4, 8
CW = 3
CH = 1

C_WALL = 1
C_FLOOR = 2
C_PATH = 3
C_IN = 4
C_OUT = 5
C_GLYPH = 6

PALETTES: dict[str, dict[str, tuple[int, int, int]]] = {
    "Neon": {
        "wall": (57, 255, 20),
        "floor": (15, 15, 25),
        "path": (255, 0, 255),
        "entry": (0, 200, 255),
        "exit": (255, 60, 60),
        "glyph": (255, 255, 0),
    },
    "Ocean": {
        "wall": (30, 90, 160),
        "floor": (5, 12, 30),
        "path": (255, 180, 50),
        "entry": (0, 230, 120),
        "exit": (220, 50, 50),
        "glyph": (140, 200, 240),
    },
    "Sunset": {
        "wall": (180, 80, 40),
        "floor": (25, 10, 15),
        "path": (240, 200, 80),
        "entry": (100, 220, 100),
        "exit": (200, 40, 80),
        "glyph": (255, 140, 100),
    },
    "Frost": {
        "wall": (130, 170, 200),
        "floor": (20, 25, 35),
        "path": (200, 100, 180),
        "entry": (50, 255, 130),
        "exit": (255, 80, 80),
        "glyph": (220, 230, 245),
    },
}


# # Converts standard RGB (0–255) colors into curses-compatible RGB
#  values (0–1000) so they can be used for custom terminal colors.
def _rgb(r: int, g: int, b: int) -> tuple[int, int, int]:
    """Scale 0-255 RGB to curses 0-1000 range.

    Args:
        r: Red.
        g: Green.
        b: Blue.

    Returns:
        Scaled (r, g, b) tuple.
    """
    return (
        int(r / 255 * 1000),
        int(g / 255 * 1000),
        int(b / 255 * 1000),
    )


# Loads a color theme (palette) into the terminal by converting RGB values
# and assigning them to curses color slots and UI color pairs used for
# rendering the maze.
def _load_palette(name: str) -> None:
    """Push a named palette into curses colour slots.

    Args:
        name: Key in PALETTES.
    """
    if not curses.can_change_color():
        return
    pal = PALETTES[name]
    curses.init_color(10, *_rgb(*pal["wall"]))
    curses.init_color(11, *_rgb(*pal["floor"]))
    curses.init_color(12, *_rgb(*pal["path"]))
    curses.init_color(13, *_rgb(*pal["entry"]))
    curses.init_color(14, *_rgb(*pal["exit"]))
    curses.init_color(15, *_rgb(*pal["glyph"]))
    curses.init_pair(C_WALL, 10, 10)
    curses.init_pair(C_FLOOR, 11, 11)
    curses.init_pair(C_PATH, 12, 12)
    curses.init_pair(C_IN, 13, 13)
    curses.init_pair(C_OUT, 14, 14)
    curses.init_pair(C_GLYPH, 15, 15)


# Sets up default terminal color pairs for the maze renderer,
# defining basic colors for walls, floor, path, entry, exit,
# and special glyphs.
def _setup_colors() -> None:
    """Initialise safe colour pairs for basic terminals."""
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(
        C_WALL, curses.COLOR_GREEN, curses.COLOR_GREEN,
    )
    curses.init_pair(
        C_FLOOR, curses.COLOR_BLACK, curses.COLOR_BLACK,
    )
    curses.init_pair(
        C_PATH, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA,
    )
    curses.init_pair(
        C_IN, curses.COLOR_CYAN, curses.COLOR_CYAN,
    )
    curses.init_pair(
        C_OUT, curses.COLOR_RED, curses.COLOR_RED,
    )
    curses.init_pair(
        C_GLYPH, curses.COLOR_YELLOW, curses.COLOR_YELLOW,
    )


# Fills the inside of a maze cell with a specific color pair at
# the correct screen position, handling coordinate offsets and safely drawing
# to the curses terminal.
def _paint_block(
    scr: "curses.window",
    mx: int, my: int,
    pair_id: int,
    ox: int, oy: int,
) -> None:
    """Fill a cell's interior with a colour pair.

    Args:
        scr: Curses window.
        mx: Cell column.
        my: Cell row.
        pair_id: Curses colour-pair index.
        ox: Terminal x offset.
        oy: Terminal y offset.
    """
    tr = oy + my * (CH + 1) + 1
    tc = ox + mx * (CW + 1) + 1
    cp = curses.color_pair(pair_id)
    try:
        for dr in range(CH):
            scr.addstr(tr + dr, tc, " " * CW, cp)
    except curses.error:
        pass


# Draws a full maze cell in the terminal, including its interior,
# walls (based on bitmask), and path-aware coloring, while handling
# edges and safely rendering with curses.
def _paint_cell(
    scr: "curses.window",
    mx: int, my: int,
    bits: int,
    pair_id: int,
    cols: int, rows: int,
    ox: int, oy: int,
    trail: Optional[list[tuple[int, int]]] = None,
) -> None:
    """Render one cell: interior, walls, and smart gap erasing.

    Args:
        scr: Curses window.
        mx: Cell column in maze coords.
        my: Cell row in maze coords.
        bits: Wall bitmask for this cell.
        pair_id: Colour pair for the cell body.
        cols: Total maze columns.
        rows: Total maze rows.
        ox: Terminal x offset.
        oy: Terminal y offset.
        trail: Solution path for context-aware colouring.
    """
    if trail is None:
        trail = []

    tr = oy + my * (CH + 1) + 1
    tc = ox + mx * (CW + 1) + 1
    wp = curses.color_pair(C_WALL)
    cp = curses.color_pair(pair_id)
    fp = curses.color_pair(C_FLOOR)

    try:
        for dr in range(CH):
            scr.addstr(tr + dr, tc, " " * CW, cp)
        scr.addstr(tr - 1, tc - 1, " ", wp)

        if bits & NORTH or my == 0:
            scr.addstr(tr - 1, tc, " " * CW, wp)
        elif pair_id == C_PATH and (mx, my - 1) not in trail:
            scr.addstr(tr - 1, tc, " " * CW, fp)
        else:
            scr.addstr(tr - 1, tc, " " * CW, cp)

        if bits & WEST or mx == 0:
            for dr in range(CH):
                scr.addstr(tr + dr, tc - 1, " ", wp)
        elif pair_id == C_PATH and (mx - 1, my) not in trail:
            for dr in range(CH):
                scr.addstr(tr + dr, tc - 1, " ", fp)
        else:
            for dr in range(CH):
                scr.addstr(tr + dr, tc - 1, " ", cp)

        if mx == cols - 1:
            for dr in range(CH + 1):
                scr.addstr(
                    tr + dr - 1, tc + CW, " ", wp,
                )
        if my == rows - 1:
            scr.addstr(
                tr + CH, tc - 1, " " * (CW + 2), wp,
            )
    except curses.error:
        pass


# Clears and redraws the entire maze frame by iterating through all cells,
# rendering each one with correct colors (including optional solution path),
# and then drawing entry/exit markers before refreshing the terminal display.
def _render(
    scr: "curses.window",
    grid: list[list[int]],
    cols: int, rows: int,
    entry: tuple[int, int],
    exit_: tuple[int, int],
    trail: Optional[list[tuple[int, int]]] = None,
    show_trail: bool = False,
    ox: int = 0, oy: int = 0,
) -> None:
    """Draw every cell of the maze onto scr.

    Args:
        scr: Curses window.
        grid: 2-D wall-bitmask list.
        cols: Maze width.
        rows: Maze height.
        entry: Entry (x, y).
        exit_: Exit (x, y).
        trail: Solution coordinates.
        show_trail: Whether to highlight the solution.
        ox: Terminal x offset.
        oy: Terminal y offset.
    """
    if trail is None:
        trail = []
    scr.clear()
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if show_trail and (c, r) in trail:
                color = C_PATH
            elif cell == 0xF:
                color = C_GLYPH
            else:
                color = C_FLOOR
            _paint_cell(
                scr, c, r, cell, color,
                cols, rows, ox, oy, trail,
            )
    _paint_block(scr, entry[0], entry[1], C_IN, ox, oy)
    _paint_block(scr, exit_[0], exit_[1], C_OUT, ox, oy)
    scr.refresh()


# Converts the shortest-path string (e.g., "EESSW") into a list of (x, y)
# coordinates by walking step-by-step from the entry to the exit using
# direction offsets.
def _trace_path(
    mg: MazeGenerator,
    entry: tuple[int, int],
    exit_: tuple[int, int],
) -> list[tuple[int, int]]:
    """Convert solver output to a coordinate list.

    Args:
        mg: Generator that has already called build().
        entry: Entry cell.
        exit_: Exit cell.

    Returns:
        Ordered list of (x, y) cells on the path.
    """
    steps = [entry]
    x, y = entry
    dirs = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    for ch in mg.shortest_path(entry, exit_):
        dx, dy = dirs[ch]
        x, y = x + dx, y + dy
        steps.append((x, y))
    return steps


_HOTKEYS: dict[int, str] = {
    ord("q"): "quit", ord("Q"): "quit",
    ord("r"): "regen", ord("R"): "regen",
    ord("h"): "trail", ord("H"): "trail",
    ord("c"): "theme", ord("C"): "theme",
}


# Displays an interactive terminal menu below the maze, allowing the
# user to navigate options (regenerate maze, toggle path, change theme,
# or quit) using arrow keys or hotkeys, and returns the selected action.
def _menu(
    scr: "curses.window",
    trail_on: bool,
    cols: int, rows: int,
    palette: str,
    ox: int, oy: int,
) -> str:
    """Arrow-key / hotkey menu below the maze.

    Args:
        scr: Curses window.
        trail_on: Current path-visibility flag.
        cols: Maze columns.
        rows: Maze rows.
        palette: Active palette name.
        ox: Terminal x offset.
        oy: Terminal y offset.

    Returns:
        Action string: regen, trail, theme, or quit.
    """
    t_label = "Hide path" if trail_on else "Show path"
    labels = [
        "[R] Regenerate",
        f"[H] {t_label}",
        f"[C] Theme ({palette})",
        "[Q] Quit",
    ]
    acts = ["regen", "trail", "theme", "quit"]
    sel = 0
    _, sw = scr.getmaxyx()
    top = oy + rows * (CH + 1) + 3
    mw = cols * (CW + 1) + 1
    cx = ox + mw // 2

    while True:
        pad = max(len(lb) for lb in labels) + 6
        for i, lb in enumerate(labels):
            lc = cx - pad // 2
            try:
                scr.addstr(top + i, 0, " " * sw)
                if i == sel:
                    scr.addstr(
                        top + i, lc,
                        f" > {lb} ", curses.A_BOLD,
                    )
                else:
                    scr.addstr(top + i, lc, f"   {lb} ")
            except curses.error:
                pass
        scr.refresh()
        k = scr.getch()

        if k in _HOTKEYS:
            return _HOTKEYS[k]
        if k == curses.KEY_UP:
            sel = (sel - 1) % len(acts)
        elif k == curses.KEY_DOWN:
            sel = (sel + 1) % len(acts)
        elif k in (curses.KEY_ENTER, 10, 13):
            return acts[sel]


# Animates the maze solution by progressively drawing each step of the path
# in order, refreshing the screen after each cell with a short delay to
# create a visual tracing effect.
def _animate_trail(
    scr: "curses.window",
    grid: list[list[int]],
    cols: int, rows: int,
    entry: tuple[int, int],
    exit_: tuple[int, int],
    trail: list[tuple[int, int]],
    ox: int, oy: int,
    ms: float = 0.02,
) -> None:
    """Draw the solution path one cell at a time.

    Args:
        scr: Curses window.
        grid: Wall grid.
        cols: Maze columns.
        rows: Maze rows.
        entry: Entry cell.
        exit_: Exit cell.
        trail: Solution coordinates.
        ox: Terminal x offset.
        oy: Terminal y offset.
        ms: Delay per cell in seconds.
    """
    for x, y in trail:
        _paint_cell(
            scr, x, y, grid[y][x], C_PATH,
            cols, rows, ox, oy, trail,
        )
        _paint_block(scr, entry[0], entry[1], C_IN, ox, oy)
        _paint_block(scr, exit_[0], exit_[1], C_OUT, ox, oy)
        scr.refresh()
        time.sleep(ms)


# Main curses application loop that initializes the maze, handles rendering,
# processes user input (menu actions like regenerate, toggle path, change
# theme, quit), and updates the display interactively in real time.
def _loop(
    scr: "curses.window",
    cols: int, rows: int,
    entry: tuple[int, int],
    exit_: tuple[int, int],
    seed: Optional[int] = None,
    perfect: bool = True,
) -> None:
    """Core event loop driven by curses.

    Args:
        scr: Curses window.
        cols: Maze width.
        rows: Maze height.
        entry: Entry cell.
        exit_: Exit cell.
        seed: Optional random seed.
        perfect: Perfect-maze flag.
    """
    _setup_colors()
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    scr.keypad(True)

    pnames = list(PALETTES)
    pidx = 0
    _load_palette(pnames[pidx])

    # keep original user intent
    user_seed = seed
    current_seed = seed if seed is not None else 42

    trail_on = False

    mg = MazeGenerator(
        cols=cols,
        rows=rows,
        seed=current_seed,
        perfect=perfect,
    )

    def offsets() -> tuple[int, int]:
        """Compute centring offsets for the current terminal."""
        sh, sw = scr.getmaxyx()
        mw = cols * (CW + 1) + 2
        mh = rows * (CH + 1) + 2
        return (
            max(0, (sw - mw) // 2),
            max(0, (sh - (mh + 6)) // 2),
        )

    ox, oy = offsets()
    mg.build(origin=entry)
    _render(
        scr, mg.walls, cols, rows, entry, exit_,
        ox=ox, oy=oy,
    )
    trail = _trace_path(mg, entry, exit_)

    while True:
        ox, oy = offsets()
        _render(
            scr, mg.walls, cols, rows, entry, exit_,
            trail, trail_on, ox, oy,
        )
        act = _menu(
            scr, trail_on, cols, rows,
            pnames[pidx], ox, oy,
        )

        if act == "quit":
            break
        elif act == "regen" and user_seed is not None:
            current_seed += 1
            mg = MazeGenerator(
                cols=cols,
                rows=rows,
                seed=current_seed,
                perfect=perfect,
            )
            mg.build(origin=entry)
            trail = _trace_path(mg, entry, exit_)
            _render(
                scr, mg.walls, cols, rows, entry, exit_,
                ox=ox, oy=oy,
            )
            if trail_on:
                _animate_trail(
                    scr, mg.walls, cols, rows,
                    entry, exit_, trail, ox, oy,
                )
        elif act == "trail":
            trail_on = not trail_on
            if trail_on:
                _animate_trail(
                    scr, mg.walls, cols, rows,
                    entry, exit_, trail, ox, oy,
                )
        elif act == "theme":
            pidx = (pidx + 1) % len(pnames)
            _load_palette(pnames[pidx])
            if trail_on:
                _render(
                    scr, mg.walls, cols, rows,
                    entry, exit_, trail, False, ox, oy,
                )
                _animate_trail(
                    scr, mg.walls, cols, rows,
                    entry, exit_, trail, ox, oy,
                )


# Public entry function that starts the curses UI by safely initializing
# the terminal and running the main event loop inside curses.wrapper().
def launch(
    cols: int, rows: int,
    entry: tuple[int, int],
    exit_: tuple[int, int],
    seed: Optional[int] = None,
    perfect: bool = True,
) -> None:
    """Public entry point for the curses display.

    Args:
        cols: Maze width in cells.
        rows: Maze height in cells.
        entry: Entry cell (x, y).
        exit_: Exit cell (x, y).
        seed: Random seed.
        perfect: Perfect-maze flag.
    """
    curses.wrapper(
        lambda s: _loop(
            s, cols, rows, entry, exit_, seed, perfect,
        ),
    )


if __name__ == "__main__":
    launch(
        cols=20, rows=15,
        entry=(0, 0), exit_=(19, 14),
    )
