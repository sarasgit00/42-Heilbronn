import sys
import math


def calculate_distance(t1: tuple, t2: tuple) -> float:
    #  power of 2 is **2
    return math.sqrt((t1[0] - t2[0])**2 +
                     (t1[1] - t2[1])**2 + (t1[2] - t2[2])**2)


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    print()

    total_args = sys.argv[1:]

    if not total_args:
        print("No coordinates were provided. Provide X, Y and Z.")
        return
    elif len(total_args) != 3:
        print("Coordinates must consists of X, Y and Z")
        return

    try:
        user_coords = [int(coordinate) for coordinate in total_args]
    except ValueError as e:
        print(f"Parsing invalid coordinates: {total_args}")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - {e.__class__.__name__}, Args: {e.args}")
        return

    origin: tuple = (0, 0, 0)

    x2 = user_coords[0]
    y2 = user_coords[1]
    z2 = user_coords[2]
    coordinates_tuple: tuple = (x2, y2, z2)

    print(f"Position created: {coordinates_tuple}")
    print(f"Distance between {origin} and {coordinates_tuple}: "
          f"{calculate_distance(coordinates_tuple, origin):.2f}")
    print()

    user_coords = ("3", "4", "0")
    user_coords = tuple(int(c) for c in user_coords)
    x2 = user_coords[0]
    y2 = user_coords[1]
    z2 = user_coords[2]
    coordinates_str: str = f"({x2}, {y2}, {z2})"
    coordinates_tuple: tuple = (x2, y2, z2)
    print(f"Parsing coordinates: {coordinates_str}")
    print(f"Parsed position: ({coordinates_str})")
    print(f"Distance beween {origin} and {coordinates_str}:"
          f" {calculate_distance(coordinates_tuple, origin):.1f}")

    print()
    print("Unpacking demonstration:")
    loc1, loc2, loc3 = user_coords
    print(f"Player at x={loc1}, y={loc2}, z={loc3}")
    print(f"Coordinates: X={loc1}, Y={loc2}, Z={loc3}")


if __name__ == "__main__":
    ft_coordinate_system()
