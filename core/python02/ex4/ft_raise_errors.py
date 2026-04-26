"""
This module provides a function to check the health of plants
based on their water level and sunlight exposure.
"""


class BadPlant(ValueError):
    pass


class BadWaterLevel(ValueError):
    pass


class SunLightHours(ValueError):
    pass


def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    """
    Check if the plant is healthy based on water level and sunlight hours.
    Raises ValueError with descriptive messages if any parameter is out of
    range.
    """
    if not plant_name:
        raise BadPlant("Plant name cannot be empty!")
    if water_level < 1:
        raise BadWaterLevel(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise BadWaterLevel(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise SunLightHours(f"Sunlight hours {sunlight_hours} is too low "
                            "(min 2)")
    if sunlight_hours > 12:
        raise SunLightHours(f"Sunlight hours {sunlight_hours} is too high"
                            "(max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    Test the plant health checker with various inputs to ensure
    that it raises appropriate errors for invalid parameters.
    """
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        result = check_plant_health("tomato", 5, 8)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except BadPlant as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except BadWaterLevel as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except SunLightHours as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
