class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass  # means "do nothing", py doesnt allow empty blocks


class PlantError(GardenError):
    """Error related to plant problems."""
    pass


class WaterError(GardenError):
    """Error related to watering problems."""
    pass


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


def ft_test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")

    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")

    try:
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")

    try:
        check_plant()
    except (GardenError) as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water()
    except (GardenError) as e:
        print(f"Caught a garden error: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_test_custom_errors()


# raise=fehler ausloesen
