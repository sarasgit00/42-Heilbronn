"""
In this exercise, we will implement a simple garden security system to protect
our plants from invalid operations. We will create a class called `SecurePlant`
hat encapsulates the properties of a plant, such as its name, height, and age.
The class will include methods to set and get these properties while ensuring
that invalid inputs (like negative height or age) are rejected.
"""


class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        print(f"Plant created: {self.name}")
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

# height&age is with _ which means "pls dont touch directly,first setting to 0"
# this is hiding data, which is called "encapsulation",because no direct access
# 0 default,because evry (user)input should be checked. age -12 e.g. is invalid
# set_height(height) is a mehtod that is controlling the input

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current plant: {self.name} ({self._height}cm, "
              f"{self._age} days)")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)

    # ODER: plant.set_height(25)
    # und: plant.set_age(30), statt die Zeile drueber

    plant.set_height(-5)

    plant.get_info()


if __name__ == "__main__":
    ft_garden_security()
