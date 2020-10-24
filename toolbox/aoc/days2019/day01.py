import math

def get_fuel_required_for_mass(mass):
    """to find the fuel required for a module, take its
    mass, divide by three, round down, and subtract 2."""
    return max(math.floor(mass/3) - 2, 0)


def get_total_fuel_required_for_mass(mass):
    fuel_for_mass = get_fuel_required_for_mass(mass)

    if not fuel_for_mass:
        return 0
    else:
        return fuel_for_mass + get_total_fuel_required_for_mass(fuel_for_mass)
