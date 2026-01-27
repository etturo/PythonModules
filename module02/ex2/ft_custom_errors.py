#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message=None) -> None:
        self.error_message = message
        super().__init__(self, message)
        return


class PlantError(GardenError):
    def __init__(self, message=None) -> None:
        self.error_message = message
        super().__init__(message)
        return

    def __str__(self) -> str:
        return ("The tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self, message=None) -> None:
        self.error_message = message
        super().__init__(message)

    def __str__(self) -> str:
        return ("Not enough water in the tank!")


if __name__ == "__main__":
    print("\n=== Custom Garden Errors Demo ===\n")
    # Trying to catch a PlantError
    print("Testing a PlantError...")
    try:
        raise PlantError("Caught PlantError")
    except PlantError as error:
        print(f"{error.error_message}: {error}")
    # Trying to catch a WaterError
    print("\nTesting a WaterError...")
    try:
        raise WaterError("Caught WaterError")
    except WaterError as error:
        print(f"{error.error_message}: {error}")
    # Trying to catch all garden errors
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("Caught PlantError")
    except GardenError as error:
        print(f"{error.error_message}: {error}")
    try:
        raise WaterError("Caught WaterError")
    except GardenError as error:
        print(f"{error.error_message}: {error}")
    print("\nAll custom error types work correctly!\n")
