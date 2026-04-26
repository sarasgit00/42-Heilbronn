"""A-Maze-ing — generate, solve, and visualise mazes."""

import sys

from config import load_config
from display import launch
from mazegen import MazeGenerator
from writer import save_maze


def main() -> None:
    """Load config, build the maze, write output, launch display."""
    if len(sys.argv) != 2:  # run command : 0 1 2 args
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)  # exit, or else it will continue and consume RAM

    # read and loads the config file and initialize the keys
    # and expects the config file path as arg
    cfg = load_config(
        sys.argv[1]
    )  # the relative path of config.txt is simply config.txt
    # the return type is dict., so the dict. is getting stored in config.
    if cfg is None:
        sys.exit(1)

    seed = cfg.get("SEED")
    perfect: bool = cfg["PERFECT"]  # stores as bool datatype(true/false)

    # these things will be grabbed from config.txt:
    mg = MazeGenerator(
        cols=cfg["WIDTH"],
        rows=cfg["HEIGHT"],
        seed=seed,
        perfect=perfect,
    )
    mg.build(origin=cfg["ENTRY"])

    # Save maze to output file (grid + entry/exit + solution path)
    save_maze(
        cfg["OUTPUT_FILE"],
        mg.hex_rows(),
        cfg["ENTRY"],
        cfg["EXIT"],
        mg.shortest_path(cfg["ENTRY"], cfg["EXIT"]),
    )

    # Launch interactive curses visualization of the maze
    launch(
        cols=cfg["WIDTH"],
        rows=cfg["HEIGHT"],
        entry=cfg["ENTRY"],
        exit_=cfg["EXIT"],
        seed=seed,
        perfect=perfect,
    )


# Entry point of the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
    except Exception as exc:
        print(f"Fatal: {exc}")
        sys.exit(1)
