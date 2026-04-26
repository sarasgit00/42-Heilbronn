class Plant:
    def __init__(self, name: str, height: int, old: int) -> None:
        self.name = name
        self.height = height
        self.old = old

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.old} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")

    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    # some random data, that will become objects once we add this to the "plants" list, see below

    plants = []
    # empty box, where we will add real plant objects or and methods
    count_plants = 0

    for data in plant_data:
        plant = Plant(data[0], data[1], data[2]) # here the data becomes object
        plants.append(plant)
        plant.get_info()
        count_plants = count_plants + 1

    print("\n")
    print(f"Total plants created: {count_plants}")

# data 0 is Rose in this case , just like index:
# data[0], data[1], data[2] --> rose, 25, 30
# data 1 is Oak in this case :
# data[0], data[1], data[2] --> oak, 200, 365
# .APPEND(plant) means add +1 "plant" in the box "plants[]"


if __name__ == "__main__":
    ft_plant_factory()
