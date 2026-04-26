class GardenError(Exception):
    pass


class BadPlant(GardenError):
    pass


class BadWaterLevel(GardenError):
    pass


class SunLightHours(GardenError):
    pass


class TankWater(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants: list[any] = []

    def add_plants(self, name: str) -> None:
        if not name:
            raise BadPlant("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        print("Watering plants...")
        print("Opening watering system")
        try:
            for i in self.plants:
                print(f"Watering {i} - success")
        except TankWater as e:
            print(f"Watering error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str, water_level: int,
                           sun_hours: int) -> None:
        print("Checking plant health...")
        if water_level > 0 and water_level < 16:
            print(f"{name}: healthy (water: {water_level}, sun: {sun_hours})")
        try:
            if water_level < 1:
                raise BadWaterLevel(f"checking {name}: Water level "
                                    f"{water_level} is too low (min 1)")
        except BadWaterLevel as e:
            print(f"Error: {e}")

        try:
            if water_level < 10:
                raise BadWaterLevel(f"checking {name}: Water level "
                                    f"{water_level} is too hight (max 10)")
        except BadWaterLevel as e:
            print(f"Error: {e}")

        try:
            if sun_hours > 12:
                raise SunLightHours(f"Sunlight hours {sun_hours} "
                                    "is too high (max 12)")
        except SunLightHours as e:
            print(f"Error: {e}")

        try:
            if sun_hours < 2:
                raise SunLightHours(f"Sunlight hours {sun_hours} "
                                    "is low high (min 2)")
        except SunLightHours as e:
            print(f"Error: {e}")


def test_garden_management() -> None:

    print("=== Garden Management System ===")
    print()

    manager = GardenManager()

    plants = ["tomato", "carrot", ""]

    try:
        print("Adding plants to garden...")
        for i in plants:
            manager.add_plants(i)
    except BadPlant as e:
        print(f"Error adding plant: {e}")

    print()
    manager.water_plants()

    print()
    manager.check_plant_health("tomato", 5, 8)

    print()
    print("Testing error recovery...")
    try:
        raise TankWater("Not enough water in tank")
    except TankWater as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
