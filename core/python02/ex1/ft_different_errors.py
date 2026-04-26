def garden_operations() -> None:
    print()
    print("Testing ValueError...")
    try:
        _ = int("miau")  # "_" is a temporary variable
    except ValueError as e:  # e is an Object of the class ValueError
        print(f"Caught ValueError: {e}")  # gives back default errormessage
    print()
    print("Testing ZeroDivisionError...")
    try:
        _ = 100 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()
    print("Testing FileNotFoundError...")
    try:
        # r is read, saving file in variable "file"
        with open("missing.txt", "r") as file:
            _ = file.read()  # inhalt wird in file gespeichert
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print()
    print("Testing KeyError...")
    try:
        # dictionary, flower=key & rose=value
        garden = {"flower": "rose", "tree": "oak"}
        _ = garden["vegetable"]  # give me the value of the key "vegetable"
    except KeyError as e:  # KeyError = Datastrucure problem
        print(f"Caught KeyError: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    garden_operations()

    print()
    print("Testing multiple errors together...")
    try:
        _ = int("hello")
        _ = 5 / 0
    except (ValueError, ZeroDivisionError) as e:
        print(f"Caught error: {e}, but program continues!")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
