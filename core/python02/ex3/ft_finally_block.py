class NoPlant(Exception):
    pass


def check_plant() -> None:
    raise NoPlant("Cannot water None - invalid plant!")
# this str now is an obj of the class NoPlant


def water_plants(plant_list: list[str]) -> None:
    try:
        print("Opening watering systems")
        for plant in plant_list:
            if plant is None:  # same as if plant == NULL
                check_plant()
            print(f"Watering {plant}")

    except NoPlant as e:
        print(f"Error: {e}")

    finally:  # finally block always runs, also whenmistake happens
        print("Closing watering systen (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    print("Testing normal watering...")
    good_plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(good_plant_list)
    print("Watering completed successfully!")

    print()
    print("Testing with error...")
    bad_plant_list = ["tomato", None]
    water_plants(bad_plant_list)

    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
