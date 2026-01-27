#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    @staticmethod
    def is_bloom() -> str:
        return ("(blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points


class GardenManager:
    garden_list = []

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name.capitalize()
        self.create_garden_network(self)
        self.plant_list = []
        print(f"Created {self.owner_name}'s garden succesfully!")

    def add_plant(self, plant: Plant) -> None:
        self.plant_list.append(plant)
        print(f"Added {plant.name.capitalize()} to {self.owner_name}'s garden")

    def grow_plants(self) -> None:
        for plant in self.plant_list:
            plant.age += 1
            plant.height += 1
            print(f"{plant.name.capitalize()} grew 1cm")

    @classmethod
    def print_stat(cls) -> None:
        print(f"{cls.GardenStats.get_stats(cls.garden_list)}")

    class GardenStats:
        @staticmethod
        def get_stats(garden_list: list) -> None:
            for garden in garden_list:
                print(f"\nPlants in {garden.owner_name.upper()}'s garden:")
                for plant in garden.plant_list:
                    attr = GardenManager.GardenStats.print_plant_attr(plant)
                    print(f"- {attr}")
            return (f"Total garden managed: {len(garden_list)}\n")

        @staticmethod
        def print_plant_attr(plant: Plant) -> str:
            if plant.__class__ == PrizeFlower:
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old, "
                        f"the flower is {plant.color} {plant.is_bloom()}, "
                        f"Prize points: {plant.prize_points}")
            elif plant.__class__ == FloweringPlant:
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old, "
                        f"the flower is {plant.color} {plant.is_bloom()}")
            elif plant.__class__ == Plant:
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old")
            else:
                return ("Unkown type")

        @staticmethod
        def print_scores(garden_list: list) -> None:
            i = 0
            print("Garden scores - ", end="")
            for garden in garden_list:
                if i > 0:
                    print(", ", end="")
                points = GardenManager.GardenStats.get_points(
                    garden.plant_list)
                print(f"{garden.owner_name}: {points}", end="")
                i += 1
            print()

        @staticmethod
        def get_points(plant_list: list) -> int:
            count = 0
            for plant in plant_list:
                if plant.__class__ == PrizeFlower:
                    count += plant.prize_points
            return count

        @staticmethod
        def height_validation(garden_list: list) -> bool:
            for garden in garden_list:
                if GardenManager.GardenStats.get_height(garden.plant_list):
                    pass
                else:
                    return print("Height validation: False")
                print("Height validation: True")

        @staticmethod
        def get_height(plant_list: list) -> bool:
            for plant in plant_list:
                if plant.height > 60:
                    return False
            return True

    @classmethod
    def create_garden_network(cls, self) -> None:
        cls.garden_list.append(self)


def main():
    # Adding Gardens
    carlo_garden = GardenManager("carlo")
    mario_garden = GardenManager("mario")
    giorgio_garden = GardenManager("giorgio")
    print()
    # Adding plant to garden
    carlo_garden.add_plant(PrizeFlower("rose", 10, 25, "red", 10))
    carlo_garden.add_plant(FloweringPlant("sunflower", 80, 15, "yellow"))
    mario_garden.add_plant(Plant("carrot", 16, 20))
    giorgio_garden.add_plant(PrizeFlower("dandelion", 15, 7, "yellow", 70))
    # Viewing the stat of the gardens
    GardenManager.print_stat()
    # Updating Gardens
    carlo_garden.grow_plants()
    mario_garden.grow_plants()
    carlo_garden.grow_plants()
    mario_garden.grow_plants()
    carlo_garden.grow_plants()
    mario_garden.grow_plants()
    # Viewing the stat of the gardens
    GardenManager.print_stat()
    # Viewing the garden's winner
    GardenManager.GardenStats.height_validation(GardenManager.garden_list)
    GardenManager.GardenStats.print_scores(GardenManager.garden_list)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    main()
    print()
