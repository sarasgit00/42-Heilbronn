from .basic import lead_to_gold  # . means from this package
from ..potions import healing_potion  # .. means from superior package


def philosophers_stone() -> str:
    return (
        f"Philosopher's stone created using {lead_to_gold()} and "
        f"{healing_potion()}"
    )


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
