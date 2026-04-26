import alchemy.elements
from alchemy.elements import create_water, create_fire, create_earth
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion as strength

print("=== Import Transmutation Mastery ===")
print()

print("Method 1 - Full module import:")
print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
print()

# from alchemy.elements import create_water
print("Method 2 - Specific function import:")
print("create_water():", create_water())
print()

# from alchemy.potions import healing_potion as heal
print("Method 3 - Aliased import:")
print("heal():", heal())
print()

print("Method 4 - Multiple imports:")
print("create_earth():", create_earth())
print("create_fire():", create_fire())
print("strength_potion():", strength())
print()

print("All import transmutation methods mastered!")
