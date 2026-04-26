import sys  # importing system library to use sys.argv


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    total_args: list = sys.argv[1:]
    number_of_args: int = len(sys.argv)
    # sys.argv is a list, [1:] skipping 1. arg which is filename

    if not total_args:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {number_of_args}")

    elif number_of_args > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Argmuments received: {number_of_args -1}")
        i = 1
        for arg in total_args:
            print(f"Arguments {i}: {arg}")
            i += 1
        print(f"Total arguments: {number_of_args}")


if __name__ == "__main__":
    ft_command_quest()
