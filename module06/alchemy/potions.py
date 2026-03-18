import alchemy.elements
from alchemy.elements import create_fire


def healing_potion() -> str:
    return (f"Healing potion brewed with {create_fire()}"
            f"and {alchemy.create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {alchemy.elements.create_earth()}"
            f"and {create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {alchemy.elements.create_air()}"
            f"and {alchemy.create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: {create_fire()},"
            f"{alchemy.elements.create_air()}, {alchemy.create_water()},"
            f"{alchemy.elements.create_earth()}")
