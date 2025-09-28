#!/usr/bin/env python3
"""
temp_conversion_tool.py
A tiny utility that converts temperatures between Celsius and Fahrenheit
while demonstrating the use of global variables for the conversion factors.
"""

# ------------------------------------------------------------------
# 1. Global conversion factors (read-only inside functions)
# ------------------------------------------------------------------
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


# ------------------------------------------------------------------
# 2. Conversion functions
# ------------------------------------------------------------------
def convert_to_celsius(fahrenheit: float) -> float:
    """
    Convert a Fahrenheit temperature to Celsius using the global factor.

    Formula: (F − 32) × 5/9
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius: float) -> float:
    """
    Convert a Celsius temperature to Fahrenheit using the global factor.

    Formula: (C × 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


# ------------------------------------------------------------------
# 3. User-interaction helper
# ------------------------------------------------------------------
def _read_numeric(prompt: str) -> float:
    """
    Read a numeric value from the user.
    Raise ValueError with the required message on invalid input.
    """
    raw = input(prompt)
    try:
        return float(raw)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


# ------------------------------------------------------------------
# 4. Main driver
# ------------------------------------------------------------------
def main() -> None:
    """Run the interactive temperature converter."""
    temp = _read_numeric("Enter the temperature to convert: ")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# ------------------------------------------------------------------
# 5. Script entry-point guard
# ------------------------------------------------------------------
if __name__ == "__main__":
    main()