"""Iterative stack-based maze generator with BFS solver.

Provides MazeGenerator which carves mazes using an explicit
stack (no recursion), stamps a 42 glyph of sealed cells, and
finds the shortest path via breadth-first search.
"""

# DFS builds the maze, BFS solves it, randomness shapes it,
# and bitmasks store it efficiently.
# A bitmask is a single number that uses binary bits to store
# multiple on/off (true/false) states at once.
# In this code, True/False = whether a wall exists in a given
# direction for a cell:
# True (bit = 1) → wall is present (blocked)
# False (bit = 0) → wall is removed (open path)

import random
from collections import deque
from typing import Iterator, Optional

# global variables:
# the walls are 1 2 4 8 and the movements are the tuples
NORTH, EAST, SOUTH, WEST = 1, 2, 4, 8
FLIP = {NORTH: SOUTH, SOUTH: NORTH, EAST: WEST, WEST: EAST}
DELTA = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0),
}
LETTERS = {NORTH: "N", EAST: "E", SOUTH: "S", WEST: "W"}

# This is just a spacing/threshold constant.
# minimum size, padding or spacing between patterns
_MIN_42 = 10

# the yellow blocks/cells inthe number 4 that shapes 4
GLYPH_4 = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 0),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
]

# the yellow blocks/cells inthe number 2 that shapes 2
GLYPH_2 = [
    (0, 0),
    (1, 0),
    (2, 0),
    (2, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (0, 3),
    (0, 4),
    (1, 4),
    (2, 4),
]


class MazeGenerator:
    """Stack-based maze generator with bitmask walls and BFS solver.

    Attributes:
        cols: Number of columns (width).
        rows: Number of rows (height).
        seed: Random seed for reproducibility.
        perfect: Whether to keep the maze as a spanning tree.
        walls: 2-D grid of wall bitmasks after build().
        carved: Set of (x, y) cells carved during generation.
    """

    # these things will be grabbed from config.txt:
    def __init__(
        self,
        cols: int,
        rows: int,
        seed: Optional[int] = None,
        perfect: bool = True,
    ) -> None:
        """Create a new generator.

        Args:
            cols: Maze width in cells.
            rows: Maze height in cells.
            seed: Optional seed for deterministic output.
            perfect: If True every pair of cells has exactly
                     one connecting path.
        """
        # initializing:
        self.cols = cols
        self.rows = rows
        self.seed = seed
        self.perfect = perfect
        self.walls: list[list[int]] = []
        self.carved: set[tuple[int, int]] = set()  # carving 42 into maze

    # carving 42 into the maze method:
    def _stamp_42(self) -> None:
        """Mark glyph cells as carved so the carver skips them."""
        if self.cols < _MIN_42 or self.rows < _MIN_42:
            print("Warning: maze too small for the 42 pattern.")
            return

        ox = self.cols // 2 - 4
        oy = self.rows // 2 - 2

        for gx, gy in GLYPH_4:
            cx, cy = ox + gx, oy + gy
            if 0 <= cx < self.cols and 0 <= cy < self.rows:
                self.carved.add((cx, cy))

        for gx, gy in GLYPH_2:
            cx, cy = ox + gx + 4, oy + gy
            if 0 <= cx < self.cols and 0 <= cy < self.rows:
                self.carved.add((cx, cy))

    # function to set the start to cell 0,0 (upper left corner)
    def _pick_start(
        self,
        preferred: tuple[int, int],
    ) -> tuple[int, int]:
        """Return preferred if valid, else first free cell.

        Args:
            preferred: Desired starting cell.

        Returns:
            An (x, y) cell that is in-bounds and not reserved.
        """
        px, py = preferred
        if (
            0 <= px < self.cols
            and 0 <= py < self.rows
            and preferred not in self.carved
        ):
            return preferred
        for r in range(self.rows):
            for c in range(self.cols):
                if (c, r) not in self.carved:
                    return (c, r)
        return (0, 0)

    # main part: DFS Algorithm = Depth-First Search
    # Go as deep as possible in one direction before coming back (like going
    # down a tunnel until it ends, then backtracking)
    def build(
        self,
        origin: tuple[int, int] = (0, 0),
    ) -> None:
        """Generate the maze with an iterative stack carver.

        Args:
            origin: Cell where carving begins.
        """
        if self.seed is not None:
            random.seed(self.seed)

        self.walls = [
            [0xF] * self.cols for _ in range(self.rows)
        ]  # forming the 4 walls
        self.carved = set()
        self._stamp_42()

        start = self._pick_start(origin)
        self.carved.add(start)  # adding starting poimt to set-list
        stack: list[tuple[int, int]] = [start]  # initialzing the list

        # key DFS part, bitmask:
        while stack:
            #
            cx, cy = stack[-1]
            neighbours = self._uncarved_around(cx, cy)
            if neighbours:
                d, nx, ny = random.choice(neighbours)
                self.walls[cy][cx] &= ~d
                self.walls[ny][nx] &= ~FLIP[d]
                self.carved.add((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()

        if not self.perfect:
            self._break_walls()

    # DFS maze generator that returns each carved cell
    # step-by-step so the process can be visualized.
    def build_animated(
        self,
        origin: tuple[int, int] = (0, 0),
    ) -> Iterator[tuple[int, int]]:
        """Like build() but yields every carved cell.

        Args:
            origin: Cell where carving begins.

        Yields:
            (x, y) of each newly opened cell.
        """
        if self.seed is not None:
            random.seed(self.seed)

        self.walls = [[0xF] * self.cols for _ in range(self.rows)]
        self.carved = set()
        self._stamp_42()

        start = self._pick_start(origin)
        self.carved.add(start)
        yield start
        stack: list[tuple[int, int]] = [start]

        while stack:
            cx, cy = stack[-1]
            neighbours = self._uncarved_around(cx, cy)
            if neighbours:
                d, nx, ny = random.choice(neighbours)
                self.walls[cy][cx] &= ~d
                self.walls[ny][nx] &= ~FLIP[d]
                self.carved.add((nx, ny))
                stack.append((nx, ny))
                yield (nx, ny)
            else:
                stack.pop()

        if not self.perfect:
            self._break_walls()

    # creating the uncarved area(non black area)
    def _uncarved_around(
        self,
        x: int,
        y: int,
    ) -> list[tuple[int, int, int]]:
        """Return (direction, nx, ny) for uncarved neighbours.

        Args:
            x: Column of the current cell.
            y: Row of the current cell.

        Returns:
            List of (direction_bit, nx, ny) tuples.
        """
        # a tuple in this maze are cells
        out: list[tuple[int, int, int]] = []
        for d, (dx, dy) in DELTA.items():
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < self.cols
                and 0 <= ny < self.rows
                and (nx, ny) not in self.carved
            ):
                out.append((d, nx, ny))
        return out

    # It randomly removes some walls to create loops and multiple paths,
    # while keeping the maze structure controlled.
    def _break_walls(self) -> None:
        """Remove random walls to add loops (non-perfect mode).

        Wall removals are filtered to preserve the subject constraint
        that no 3x3 fully-open area may appear.
        """
        pool: list[tuple[int, int, int]] = []
        for r in range(self.rows):
            for c in range(self.cols):
                if self.walls[r][c] == 0xF:
                    continue
                for d in (EAST, SOUTH):
                    if not (self.walls[r][c] & d):
                        continue
                    dx, dy = DELTA[d]
                    nc, nr = c + dx, r + dy
                    if (
                        0 <= nc < self.cols
                        and 0 <= nr < self.rows
                        and self.walls[nr][nc] != 0xF
                    ):
                        pool.append((c, r, d))
        random.shuffle(pool)
        limit = max(1, len(pool) // 8)
        opened = 0
        for c, r, d in pool:
            if opened >= limit:
                break
            dx, dy = DELTA[d]
            nc, nr = c + dx, r + dy
            if not self._can_open_wall_without_3x3(c, r, d, nc, nr):
                continue
            self.walls[r][c] &= ~d
            self.walls[nr][nc] &= ~FLIP[d]
            opened += 1

    # It tests if removing a wall is safe, withoutpermanently changing the maze
    def _can_open_wall_without_3x3(
        self,
        c: int,
        r: int,
        d: int,
        nc: int,
        nr: int,
    ) -> bool:
        """Dry-run a wall removal and reject it
          if it creates a 3x3 open area."""
        wall_a = self.walls[r][c]
        wall_b = self.walls[nr][nc]
        self.walls[r][c] = wall_a & ~d
        self.walls[nr][nc] = wall_b & ~FLIP[d]
        ok = self.check_no_3x3_open()
        self.walls[r][c] = wall_a
        self.walls[nr][nc] = wall_b
        return ok

    # BFS (Breadth-First Search)
    # Explore all nearby options first, then go further (like spreading out in
    # circles from the start), to find the shortest path
    def shortest_path(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> str:
        """BFS shortest path between two cells.

        Args:
            start: Source cell (x, y).
            end: Destination cell (x, y).

        Returns:
            Direction string like "EESSW", or "" if unreachable.
        """
        seen: set[tuple[int, int]] = {start}
        queue: deque[tuple[tuple[int, int], str]] = deque(
            [(start, "")],
        )
        # Uses a FIFO queue to process cells in order of discovery,
        # ensuring the first time we reach the end is the shortest path.
        while queue:
            (x, y), trail = queue.popleft()
            if (x, y) == end:
                return trail
            for d, (dx, dy) in DELTA.items():
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < self.cols
                    and 0 <= ny < self.rows
                    and not (self.walls[y][x] & d)
                    and (nx, ny) not in seen
                ):
                    seen.add((nx, ny))
                    queue.append(
                        ((nx, ny), trail + LETTERS[d]),
                    )
        return ""

    # It checks the whole maze to ensure there are no fully open 3×3 spaces.
    def check_no_3x3_open(self) -> bool:
        """Verify no 3x3 fully-open area exists.

        Returns:
            True when the constraint holds.
        """
        for r in range(self.rows - 2):
            for c in range(self.cols - 2):
                blocked = False
                for dr in range(3):
                    for dc in range(3):
                        if dc < 2 and (self.walls[r + dr][c + dc] & EAST):
                            blocked = True
                        if dr < 2 and (self.walls[r + dr][c + dc] & SOUTH):
                            blocked = True
                        if blocked:
                            break
                    if blocked:
                        break
                if not blocked:
                    return False
        return True

    # It converts the maze grid into hex strings for saving to a file.
    def hex_rows(self) -> list[str]:
        """Return one hex string per row for the output file.

        Returns:
            List of strings, each cell a single hex digit.
        """
        return ["".join(format(c, "X") for c in row) for row in self.walls]
