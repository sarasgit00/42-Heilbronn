"""Output-file writer for A-Maze-ing.

Serialises the generated maze into the hexadecimal format
required by the subject and appends entry, exit, and path data.
"""
# It writes the maze rows, the entry point, the exit point,
# and the solution path into a file so it can be stored or reused later.


def save_maze(
    dest: str,
    hex_rows: list[str],
    entry: tuple[int, int],
    exit_: tuple[int, int],
    solution: str,
) -> None:
    """Write the maze data to dest.

    Args:
        dest: Output file path.
        hex_rows: Hex-encoded maze rows.
        entry: Entry cell (x, y).
        exit_: Exit cell (x, y).
        solution: Shortest path as N/E/S/W string.
    """
    try:
        with open(dest, "w") as fh:
            for row in hex_rows:
                fh.write(row + "\n")
            fh.write("\n")
            fh.write(f"{entry[0]},{entry[1]}\n")
            fh.write(f"{exit_[0]},{exit_[1]}\n")
            fh.write(solution + "\n")
    except IOError as err:
        print(f"Error: cannot write '{dest}' — {err}")
