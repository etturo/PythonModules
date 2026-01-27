#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message=None):
        self.error_message = message
        super().__init__(self, message)

    def __str__(self):
        return ("The tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self, message=None):
        self.error_message = message
        super().__init__(message)

    def __str__(self):
        return ("Not enough water in the tank!")


if __name__ == "__main__":
    print("\n=== Custom Garden Errors Demo ===\n")
    # Trying to catch a PlantError
    try:
        print("Testing a PlantError...")
        raise GardenError("Caught PlantError: ")
    except GardenError as error:
        print(f"Error: {error}")
    # Trying to catch a WaterError
    try:
        print("\nTesting a WaterError...")
        raise WaterError("Caught WaterPlant: ")
    except WaterError as error:
        print(f"Error: {error}")
    
    print("\nAll custom error types work correctly!\n")
