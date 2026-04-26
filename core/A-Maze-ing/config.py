"""Configuration loader for A-Maze-ing.

Reads KEY=VALUE pairs from a plain-text file, validates every
field, and returns a ready-to-use dictionary or None on failure.
"""

from typing import Any

_MANDATORY = frozenset(  # frozenset: the keys will never change
    {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
)


# this is the function for config.txt
def load_config(path: str) -> dict[str, Any] | None:
    """Load and validate a configuration file.

    Args:
        path: File system path to the config file.

    Returns:
        Parsed configuration dict, or None when invalid.
    """
    cfg: dict[str, object] = {}

    # enumerate is a class. gives 1,2.. etc per line in config.txt
    try:  # try, because we use open() to open config.txt
        with open(path, "r") as fh:  # with means: opening in mode "r" (read)
            for num, raw in enumerate(fh, 1):
                line = raw.strip()  # we store the whole line without whitespce
                if not line or line.startswith("#"):
                    continue  # skips the line
                if "=" not in line:
                    print(f"Error (line {num}): missing '=' in " f"'{line}'.")
                    return None
                key, val = line.split("=", 1)
                key = key.strip().upper()  # upper() -> capitalizing
                val = val.strip()

                # if current index is 1 of these 3 it'll start storing the keys
                # and values into the dict.cfg and cast the values to integers:
                if key in ("WIDTH", "HEIGHT", "SEED"):  # tupple
                    cfg[key] = int(val)
                elif key in ("ENTRY", "EXIT"):
                    parts = val.split(",")
                    if len(parts) != 2:
                        print(f"Error: {key} needs 'x,y' " f"(got '{val}').")
                        return None
                    cfg[key] = (int(parts[0]), int(parts[1]))
                elif key == "PERFECT":
                    lv = val.lower()  # lv = values in dicts are always small
                    if lv not in ("true", "false"):  # if lowervalue not tr/fls
                        print(
                            f"Error: PERFECT accepts "
                            f"True/False (got '{val}')."
                        )
                        return None
                    # if lv is"true", store it in dict. as value
                    cfg[key] = lv == "true"
                else:
                    cfg[key] = val
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
        return None
    except ValueError as err:
        print(f"Error: bad value in config — {err}")
        return None

    # if a mandatory key missing we store it in absent, we do _mandatory minus
    # the keys stored
    absent = _MANDATORY - cfg.keys()
    if absent:
        print(f"Error: missing key(s): " f"{', '.join(sorted(absent))}")
        return None

    # Now we extract the values from the dict(that we recently filled up) with
    # the for loop above
    w, h = cfg.get("WIDTH"), cfg.get("HEIGHT")
    if not isinstance(w, int) or not isinstance(h, int):  # checkifvalsare ints
        print("Error: WIDTH/HEIGHT must be integers.")
        return None
    if w < 1 or h < 1:
        print(f"Error: dimensions must be > 0 ({w}x{h}).")
        return None

    entry = cfg.get("ENTRY")
    exit_ = cfg.get("EXIT")
    if not isinstance(entry, tuple) or len(entry) != 2:
        print("Error: ENTRY must be 'x,y'.")
        return None
    if not isinstance(exit_, tuple) or len(exit_) != 2:
        print("Error: EXIT must be 'x,y'.")
        return None

    ex, ey = entry
    ox, oy = exit_
    if not (0 <= ex < w and 0 <= ey < h):
        print(f"Error: ENTRY {entry} outside {w}x{h} grid.")
        return None
    if not (0 <= ox < w and 0 <= oy < h):
        print(f"Error: EXIT {exit_} outside {w}x{h} grid.")
        return None
    if entry == exit_:
        print("Error: ENTRY and EXIT must be different.")
        return None

    return cfg
