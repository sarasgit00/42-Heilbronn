from typing import Any


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, cm: int) -> None:
        self.height = self.height + cm
        return print(f"{self.name} has grown by {cm}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def __str__(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.color} flowers "
                f"(blooming), Prize points: {self.points}")


class GardenManager:

    total_gardens: int = 0

    class GardenStats:
        def calculate_points(self, plants: list[Plant]) -> int:
            height_score = 0
            for i in plants:
                height_score += i.height
                if hasattr(i, 'points'):  # hasattr=has attribute ( built in )
                    height_score += i.points * 10
            return height_score

    def __init__(self, name: str) -> None:
        self.name = name
        self.plants: list[Plant] = []
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Any) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:

        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(1)

    def generate_report(self) -> None:
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            if isinstance(p, PrizeFlower):
                print(p)
            elif isinstance(p, FloweringPlant):
                print(f"{p.name}: {p.height}cm, {p.color} flowers (blooming)")
            else:
                print(f"{p.name}: {p.height}cm")

        print(f"Plants added: {len(self.plants)}")

        score = self.stats.calculate_points(self.plants)
        print(f"Garden score for {self.name}: {score}")

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> list['GardenManager']:
        return [cls(owner) for owner in owners]

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


def main() -> None:
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")

    p1 = Plant("Oak Tree", 100)
    p2 = FloweringPlant("Rose", 25, "red")
    p3 = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(p1)
    alice_garden.add_plant(p2)
    alice_garden.add_plant(p3)
    print()

    alice_garden.grow_all()
    print()
    alice_garden.generate_report()
    print()

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    bob_garden = GardenManager("Bob")
    bob_garden.add_plant(Plant("Bush", 90))
    bob_score = bob_garden.stats.calculate_points(bob_garden.plants)

    print(f"Garden scores Alice: "
          f"{alice_garden.stats.calculate_points(alice_garden.plants)}, "
          f"Bob: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
