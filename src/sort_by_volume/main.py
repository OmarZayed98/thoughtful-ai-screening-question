

# Sorting thresholds (constants)
from enum import Enum


MAX_VOLUME_CM3 = 1_000_000      # Volume threshold for bulky classification
MAX_DIMENSION_CM = 150          # Dimension threshold for bulky classification
HEAVY_MASS_KG = 20              # Mass threshold for heavy classification

def sort(width, height, length, mass) -> str:
    """
    Sort package into STANDARD, SPECIAL, or REJECTED.

    args:
        width: in cm
        height: in cm
        length: in cm
        mass: in kg

    Inputs may be ints/floats
    Raises ValueError on invalid or negative inputs.
    
    Rules:
    Bulky: volume >= 1_000_000 cm^3 OR any dimension >= 150 cm
    Heavy: mass >= 20 kg

    Classifications:
    - STANDARD: standard packages (those that are not bulky or heavy) can be handled normally.
    - SPECIAL: packages that are either heavy or bulky can't be handled automatically.
    - REJECTED: packages that are both heavy and bulky are rejected.

    Returns: "STANDARD" | "SPECIAL" | "REJECTED"
    """

    def _num(x, name):
        try:
            v = float(x)
        except (TypeError, ValueError):
            raise ValueError(f"{name} must be a number or numeric string")
        if v < 0:
            raise ValueError(f"{name} cannot be negative")
        return v
    
    # cast the inputs to float
    w = _num(width, "width")
    h = _num(height, "height")
    l = _num(length, "length")
    m = _num(mass, "mass")

    # calculate the volume
    volume = w * h * l

    # check with the thresholds to determine classification
    bulky = (volume >= MAX_VOLUME_CM3) or (max(w, h, l) >= MAX_DIMENSION_CM)
    heavy = (m >= HEAVY_MASS_KG)
    
    return "REJECTED" if (bulky and heavy) else ("SPECIAL" if (bulky or heavy) else "STANDARD")

def main():
    # quick example 
    w = input("Enter width (cm): ")
    h = float(input("Enter height (cm): "))
    l = float(input("Enter length (cm): "))
    m = float(input("Enter mass (kg): "))

    result = sort(w, h, l, m)
    print(f"Classification: {result}")