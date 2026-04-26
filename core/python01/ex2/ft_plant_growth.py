class Plant:
    def __init__(self, name: str, height: int, old: int) -> None:
        self.name = name
        self.height = height
        self.old = old

    def grow(self) -> None:
        self.height = self.height + 1

    def age(self) -> None:
        self.old = self.old + 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.old} days old")


def ft_plant_grow() -> None:
    rose = Plant("Rose", 25, 30)

    start_height = rose.height

    print("=== Day 1 ===")
    rose.get_info()

    for day in range(6):
        rose.grow()
        rose.age()

    print("=== Day 7 ===")
    rose.get_info()

    growth = rose.height - start_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    ft_plant_grow()
