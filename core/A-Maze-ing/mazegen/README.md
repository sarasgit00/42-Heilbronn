# mazegen — Reusable Maze Generator

A pip-installable Python module that generates mazes using an iterative
stack-based depth-first carver and solves them with breadth-first search.

## Install

```bash
pip install mazegen_sabo_gla_bgebreeg-1.0.0-py3-none-any.whl
# or
pip install mazegen_sabo_gla_bgebreeg-1.0.0.tar.gz
```

## Quick Start

```python
from mazegen import MazeGenerator

mg = MazeGenerator(cols=20, rows=15, seed=42)
mg.build()
print(mg.shortest_path((0, 0), (19, 14)))
```

## Constructor

| Arg       | Type           | Default | Description                            |
| --------- | -------------- | ------- | -------------------------------------- |
| `cols`    | `int`          | —       | Width in cells                         |
| `rows`    | `int`          | —       | Height in cells                        |
| `seed`    | `Optional[int]`| `None`  | Seed for reproducibility               |
| `perfect` | `bool`         | `True`  | Single-path maze when True             |

## Methods

### `build(origin=(0, 0))`

Carve the maze starting at *origin*.  Must be called before any other
method that reads the grid.

### `build_animated(origin=(0, 0))`

Same as `build` but yields `(x, y)` for each carved cell, enabling
step-by-step visualisation.

### `shortest_path(start, end) -> str`

BFS shortest path.  Returns a direction string like `"EESSW"`.

### `hex_rows() -> list[str]`

One hex string per row — each cell is a single hex digit encoding its
four wall bits.

### `check_no_3x3_open() -> bool`

Returns `True` when the maze has no 3x3 fully-open zone.

## Grid Access

After `build()`:

- **`mg.walls`** — `list[list[int]]`, each int is a 4-bit wall mask.
- **`mg.carved`** — `set[tuple[int,int]]` of cells touched by the carver.
  Glyph cells have `walls[y][x] == 0xF` and appear in `carved`.

### Bitmask

| Bit | Value | Direction |
| --- | ----- | --------- |
| 0   | 1     | North     |
| 1   | 2     | East      |
| 2   | 4     | South     |
| 3   | 8     | West      |

## Algorithms

| Task       | Algorithm                           |
| ---------- | ----------------------------------- |
| Generation | Iterative DFS with explicit stack   |
| Solving    | Breadth-first search (BFS)          |
