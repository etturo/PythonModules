#!/usr/bin/env python3
class GardenError(Exception):
    pass


def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> None:
    try:
        if plant_name == "" or plant_name is None:
            raise GardenError("Plant name cannot be empty!")
        if water_level < 1:
            raise GardenError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise GardenError(f"Water level {water_level} "
                              "is too high (max 10)")
        if sunlight_hours < 2:
            raise GardenError(f"Sunlight hours {sunlight_hours} "
                              "is too low (min 2)")
        if sunlight_hours > 12:
            raise GardenError(f"Sunlight hours {sunlight_hours} "
                              "is too high (max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except GardenError as e:
        print(f"Error: {e}")


def test_plant_checks():
    print("Testing good values...")
    check_plant_health("tomato", 5, 10)
    print()
    print("Testing empty plant name...")
    check_plant_health("", 5, 10)
    print()
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 10)
    check_plant_health("tomato", 0, 10)
    print()
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, 1)
    check_plant_health("tomato", 5, 13)
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    print("\n=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print()
