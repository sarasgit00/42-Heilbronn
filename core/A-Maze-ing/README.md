*This project has been created as part of the 42 curriculum by sabo-gla, bgebreeg.*

# A-Maze-ing

## Description

A-Maze-ing generates random mazes, solves them, and lets you explore
the result in a colour-themed terminal UI.  It reads a simple text
configuration, produces an output file in hexadecimal wall encoding,
and launches an interactive `curses` display with keyboard shortcuts
for regeneration, path toggling, and palette switching.

Highlights:

- **Iterative stack-based** maze carving — no recursion limit needed.
- **Perfect and non-perfect** modes controlled by the `PERFECT` flag.
- **42 glyph** embedded as sealed cells in the maze centre (skipped
  for very small mazes with a console warning).
- **BFS solver** returning the guaranteed shortest path.
- **Four colour palettes** (Neon / Ocean / Sunset / Frost).
- **Hotkeys** for instant interaction — `R`, `H`, `C`, `Q`.
- **Reusable `mazegen` package** installable via `pip`.

## Instructions

### Install dependencies

```bash
make install
```

### Run

```bash
make run
```

or:

```bash
python3 a_maze_ing.py config.txt
```

### Lint (flake8 + mypy)

```bash
make lint
```

### Debug

```bash
make debug
```

### Clean caches

```bash
make clean
```

### Build the pip package

```bash
make build
```

Produces `.tar.gz` and `.whl` at the repository root.

## Configuration File

One `KEY=VALUE` per line.  Lines starting with `#` are comments.

| Key           | Description                     | Example               |
| ------------- | ------------------------------- | --------------------- |
| `WIDTH`       | Columns (cells)                 | `WIDTH=20`            |
| `HEIGHT`      | Rows (cells)                    | `HEIGHT=15`           |
| `ENTRY`       | Entry cell `x,y`                | `ENTRY=0,0`           |
| `EXIT`        | Exit cell `x,y`                 | `EXIT=19,14`          |
| `OUTPUT_FILE` | Destination path                | `OUTPUT_FILE=maze.txt`|
| `PERFECT`     | Perfect maze flag               | `PERFECT=True`        |
| `SEED`        | Optional reproducibility seed   | `SEED=42`             |

Default file shipped: `config.txt`.

### Error handling

The loader rejects and prints a clear message for:

- Missing required key.
- Line without `=`.
- Non-integer width, height, or seed.
- `PERFECT` not `True` or `False`.
- Malformed or out-of-bounds `ENTRY` / `EXIT`.
- `ENTRY` equal to `EXIT`.
- Zero or negative dimensions.

The program never crashes on bad input — it exits with code 1 and an
explanation.

## Algorithms

### 1 — Maze generation: iterative DFS with explicit stack

Instead of recursive backtracking the generator uses a `while` loop
and a plain Python list as an explicit stack:

1. Push the start cell and mark it *carved*.
2. Peek at the top of the stack.  Collect all uncarved neighbours.
3. If any exist, pick one at random, clear the wall between the two
   cells on both sides, push the new cell, and mark it carved.
4. Otherwise pop (backtrack).
5. Repeat until the stack is empty.

This avoids Python's recursion limit entirely and behaves identically
to the recursive variant in terms of maze quality.

When `PERFECT=False`, a post-processing pass randomly removes roughly
12 % of remaining internal walls, introducing loops.

### 2 — Path solving: breadth-first search

BFS explores cells layer by layer using a FIFO queue, recording the
direction string at every step.  The first time the exit is dequeued
the accumulated string is the shortest path — guaranteed by BFS's
level-order property.

### Why these choices?

- **Iterative DFS** produces the same long-winding corridors as the
  recursive version but works on arbitrarily large mazes without
  touching `sys.setrecursionlimit`.
- **BFS** is the simplest algorithm that guarantees shortest paths
  without needing a heuristic or edge weights.

## Display

Built with Python `curses`.  All hotkeys work at any time.

| Key / Action       | Effect                                     |
| ------------------ | ------------------------------------------ |
| Arrow keys + Enter | Navigate the menu                          |
| **R**              | Regenerate (increments seed)               |
| **H**              | Toggle shortest-path animation             |
| **C**              | Cycle palette (Neon → Ocean → Sunset → Frost) |
| **Q**              | Quit                                       |

## Reusable Module (`mazegen`)

The generation + solving logic lives in `mazegen/` and ships as a
standalone pip package.  Documentation for the module is bundled inside
the package itself (see `mazegen/README.md`).

### Build

```bash
make build
```

### Install (in any virtualenv)

```bash
pip install mazegen_sabo_gla_bgebreeg-1.0.0-py3-none-any.whl
```

### Usage

```python
from mazegen import MazeGenerator

mg = MazeGenerator(cols=20, rows=15, seed=42)
mg.build()

# grid access
print(mg.walls)          # 2-D list of 4-bit ints
print(mg.hex_rows())     # hex-encoded rows

# solve
path = mg.shortest_path((0, 0), (19, 14))
print(path)              # "EESSW..."
```

| Parameter | Type           | Default | Description              |
| --------- | -------------- | ------- | ------------------------ |
| `cols`    | `int`          | —       | Width in cells           |
| `rows`    | `int`          | —       | Height in cells          |
| `seed`    | `Optional[int]`| `None`  | Seed for reproducibility |
| `perfect` | `bool`         | `True`  | Single-path maze         |

| Method                 | Returns     | Description                  |
| ---------------------- | ----------- | ---------------------------- |
| `build(origin)`        | `None`      | Carve the maze               |
| `build_animated(origin)` | iterator | Carve, yielding each cell    |
| `shortest_path(s, e)`  | `str`       | BFS shortest path            |
| `hex_rows()`           | `list[str]` | Hex output rows              |
| `check_no_3x3_open()`  | `bool`      | Validate corridor constraint |

## Team & Project Management

### Roles

- **sabo-gla** — maze generator module, package build, config loader,
  output writer.
- **bgebreeg** — terminal display, entry point, Makefile, integration.
- Both — code review, testing, config-file design.

### Planning

We split the work into two tracks (generator vs. display) and used
feature branches with regular syncs.  Initial planning gave each track
one week; in practice the display needed an extra couple of days for
colour-theme tuning and hotkey support, while the generator finished
ahead of schedule.

### What went well

Clear ownership of modules meant we rarely blocked each other.
The bitmask wall scheme turned out to be a natural fit for both the
generator and the renderer, so integration was smooth.

### What could be improved

We underestimated the time needed to test edge-case configs
(zero-size mazes, entry == exit, letters in numeric fields).
Building a small pytest suite earlier would have saved manual testing
time towards the end.

### Tools

- VS Code
- Git with feature branches
- pip / venv
- flake8, mypy, pytest
- `python3 -m build` for packaging

## Resources

- [Maze generation algorithm — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Depth-first search — Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
- [Breadth-first search — Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Think Labyrinth — maze algorithms](https://www.astrolog.org/labyrnth/algrithm.htm)
- [Python curses docs](https://docs.python.org/3/library/curses.html)
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/)

### AI Usage

AI tools were used for:

- Drafting the initial project plan and file-responsibility split.
- Reviewing code against flake8 and mypy requirements.
- Suggesting improvements to error messages in the config loader.
- Generating boilerplate for docstrings and type hints.

All algorithmic logic was implemented and validated by the team.
