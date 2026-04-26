import alchemy.grimoire as grimoire

print("=== Circular Curse Breaking ===")
print()

print("Testing ingredient validation:")
print(
    'validate_ingredients("fire air"):',
    grimoire.validate_ingredients("fire air"),
)
print(
    'validate_ingredients("dragon scales"):',
    grimoire.validate_ingredients("dragon scales"),
)
print()

print("Testing spell recording with validation:")
print(
    'record_spell("Fireball", "fire air"):',
    grimoire.record_spell("Fireball", "fire air"),
)
print(
    'record_spell("Dark Magic", "shadow"):',
    grimoire.record_spell("Dark Magic", "shadow"),
)
print()

print("Testing late import technique:")
print(
    'record_spell("Lightning", "air"):',
    grimoire.record_spell("Lightning", "air"),
)
print()

print("Circular dependency curse avoided using late imports!")
print("All spells processed safely!")
