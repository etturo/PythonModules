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
        cls.GardenStats.get_stats(cls.garden_list)

    class GardenStats:
        @staticmethod
        def get_stats(garden_list: list):
            for garden in garden_list:
                print(f"\nPlants in {garden.owner_name.upper()}'s garden:")
                for plant in garden.plant_list:
                    attr = GardenManager.GardenStats.get_plant_attr(plant)
                    print(f"- {attr}")
            print(f"Total garden managed: {len(garden_list)}\n")

        @staticmethod
        def get_plant_attr(plant: Plant) -> str:
            if isinstance(plant, PrizeFlower):
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old, "
                        f"the flower is {plant.color} {plant.is_bloom()}, "
                        f"Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old, "
                        f"the flower is {plant.color} {plant.is_bloom()}")
            elif isinstance(plant, Plant):
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old")
            else:
                return ("Unkown type")

        @staticmethod
        def disp_leaderboard(garden_list: list):
            print("The leaderboard is:")
            garden_list.sort(
                key=lambda g: GardenManager.GardenStats.get_points(
                    g.plant_list),
                reverse=True)
            for garden in garden_list:
                points = GardenManager.GardenStats.get_points(
                    garden.plant_list)
                print(f"{garden.owner_name}: {points}")

        @staticmethod
        def get_points(plant_list: list) -> int:
            count = 0
            for plant in plant_list:
                if (isinstance(plant, PrizeFlower)):
                    count += plant.prize_points
            return count

    @classmethod
    def create_garden_network(cls, self) -> None:
        cls.garden_list.append(self)


def main():
    # Adding Gardens
    carlo_garden = GardenManager("carlo")
    mario_garden = GardenManager("mario")
    giorgio_garden = GardenManager("giorgio")
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
    GardenManager.GardenStats.disp_leaderboard(GardenManager.garden_list)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    main()
    print()
