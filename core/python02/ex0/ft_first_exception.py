def check_temperature(temp_str: str) -> None:
    try:
        temp_int = int(temp_str)
        if (temp_int <= 40 and temp_int >= 0):
            print(f"Temperature {temp_int}°C is perfect for plants!")
        elif (temp_int > 40):
            print(f"Error: {temp_int} is too hot for plants (max 40°C)")
        elif (temp_int < 0):
            print(f"Error: {temp_int} is too cold for plants (min 0°C)")
    except ValueError:  # catches error if conversion doesnt work
        print(f"Error: '{temp_str}' is not a valid number")

# except "ValueError" oder except "Exception" (for general errors)


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    print("Testing temperature: 25")
    check_temperature("25")
    print()
    print("Testing temperature: abc")
    check_temperature("abc")
    print()
    print("Testing temperature: 100")
    check_temperature("100")
    print()
    print("Testing temperature: -50")
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
