#!/usr/bin/env python3
class GardenError(Exception):
    pass


class Plant:
    def __init__(self, name: str, water_level: int = 0):
        try:
            if name is None or name == "":
                self.name = "ERROR"
                raise GardenError("Plant name cannot be empty!")
            if water_level < 0:
                self.name = "ERROR"
                raise GardenError("Water level cannot be negative!")
            self.name = name
            self.water_level = water_level
            return print(f"Added {name} succesfully")
        except GardenError as e:
            print(f"Error adding plant: {e}")


class GardenManager:
    plant_list: Plant = []
    water_tank = 10

    def __init__(self, garden_name: str):
        self.name = garden_name
        return

    @classmethod
    def add_plant(cls, plant: Plant) -> None:
        if plant.name == "ERROR":
            return
        cls.plant_list.append(plant)
        return

    @classmethod
    def check_plant_health(cls) -> None:
        try:
            for plant in cls.plant_list:
                if plant.name == "" or plant.name is None:
                    raise GardenError("Plant name cannot be empty!")
                if plant.water_level < 1:
                    raise GardenError(f"Water level {plant.water_level} "
                                      "is too low (min 1)")
                if plant.water_level > 10:
                    raise GardenError(f"Water level {plant.water_level} "
                                      "is too high (max 10)")
                print(f"{plant.name}: is healthy! "
                      f"(water: {plant.water_level})")
        except GardenError as e:
            print(f"Error: {e}")

    @classmethod
    def water_plants(cls) -> None:
        try:
            print("Opening watering system")
            for plant in cls.plant_list:
                if cls.water_tank <= 0:
                    raise GardenError("Not enough water in tank")
                plant.water_level += 1
                cls.water_tank -= 1
                print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")
        return


def test_garden_management():
    print("Adding plant to the garden...")
    GardenManager.add_plant(Plant("Tomato", 7))
    GardenManager.add_plant(Plant("lettuce", 3))
    GardenManager.add_plant(Plant(""))
    print()
    print("Watering plants...")
    GardenManager.water_plants()
    print()
    print("Checking plant health...")
    GardenManager.check_plant_health()
    print()
    for i in range(1, 4):
        GardenManager.water_plants()
        print()
    print("Checking plant health...")
    GardenManager.check_plant_health()
    print()
    for i in range(1, 4):
        GardenManager.water_plants()
        print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    print("\n=== Garden Management System ===\n")
    test_garden_management()
    print()
