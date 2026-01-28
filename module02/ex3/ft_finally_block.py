#!/usr/bin/env python3
class GardenError(Exception):
    pass


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant in ["tomato", "lettuce", "carrots"]:
                print(f"Watering {plant}")
            else:
                raise GardenError("invalid plant")
    except GardenError as e:
        print(f"Error: Cannot water None - {e}!")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("\n=== Garden Watering System ===\n")
    plant_list = ["tomato", "lettuce", "carrots"]
    error_list = ["tomato", "pierino"]
    print("Testing normal watering...")
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(error_list)
    print()
    print("Cleanup always happens, even with errors!")
    print()
