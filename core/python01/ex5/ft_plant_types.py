class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)  # how to inherite from other class
        self.color = color

    def bloom(self) -> str:
        return print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        """
        # int,so it doesnt become float
        """
        shadow_squ = int(self.height * 0.10 + self.trunk_diameter)
        return print(f"Oak provides {shadow_squ} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self) -> str:
        return f"{self.name} is rich in vitamin {self.nutritional_value}"


def ft_plant_types_1() -> None:
    print("=== Garden Plant Types ===")
    print()  # jump a line
    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.name} (Flower): {rose.height}cm,"
          f" {rose.age} days, {rose.color} color")
    rose.bloom()
    print()
    oak = Tree("Oak", 500, 1825, 50)
    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days,"
          f" {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    print(f"{tomato.name} (Vegetable): {tomato.height}cm,"
          f" {tomato.age} days, {tomato.harvest_season} harvest")
    print(tomato)


def ft_plant_types_2() -> None:
    print("=== Garden Plant Types V2 ===")
    print()  # jump a line
    lily = Flower("Lily", 26, 31, "red")
    print(f"{lily.name} (Flower): {lily.height}cm,"
          f" {lily.age} days, {lily.color} color")
    lily.bloom()
    print()
    hazelnut = Tree("Hazelnut", 501, 1826, 51)
    print(f"{hazelnut.name} (Tree): {hazelnut.height}cm, {hazelnut.age} days,"
          f" {hazelnut.trunk_diameter}cm diameter")
    hazelnut.produce_shade()
    print()
    cucumber = Vegetable("Cucumber", 81, 91, "spring", "D")
    print(f"{cucumber.name} (Vegetable): {cucumber.height}cm,"
          f" {cucumber.age} days, {cucumber.harvest_season} harvest")
    print(cucumber)


if __name__ == "__main__":
    ft_plant_types_1()
    print()
    ft_plant_types_2()
