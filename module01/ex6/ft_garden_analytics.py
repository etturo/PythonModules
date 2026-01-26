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
        return ("(blooming!)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points


class GardenManager:
    garden_list = []

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name.capitalize()
        self.create_garden_newtwork(self)
        self.plant_list = []
        print(f"Created {self.owner_name}'s garden succesfully!")

    def add_plant(self, plant: Plant) -> None:
        self.plant_list.append(plant)
        print(f"Added {plant.name.capitalize()} to {self.owner_name}'s garden")

    def grow_plants(self) -> None:
        for plant in self.plant_list:
            plant.age += 1
            plant.height += 1

    def print_stat(self) -> None:
        self.GardenStats.get_stats(self.garden_list)

    class GardenStats:
        def get_stats(self, garden_list: list):
            count = 0
            for garden in garden_list:
                print(f"GARDEN OF: {garden.name} HAS")
                for plant in garden_list[count].plant_list:
                    print(self.get_plant_attr(plant))
                count += 1
            print(f"Total garden managed: {count}")

        def get_plant_attr(plant) -> str:
            if isinstance(plant, Plant):
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old")
            elif isinstance(plant, FloweringPlant):
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old, "
                        f"the flower is {plant.color} {plant.is_bloom()}")
            elif isinstance(plant, PrizeFlower):
                return (f"{plant.name}: {plant.height}cm, "
                        f"{plant.age} days old, "
                        f"the flower is {plant.color} {plant.is_bloom()}, "
                        f"Prize points: {plant.prize_points}")
            else:
                return ("Unkown type")

    @classmethod
    def create_garden_newtwork(cls, self) -> None:
        cls.garden_list.append(self)


def main():
    carlo_garden = GardenManager("carlo")
    mario_garden = GardenManager("mario")
    carlo_garden.add_plant(PrizeFlower("rose", 10, 25, "red", 10))
    mario_garden.add_plant(Plant("carrot", 16, 20))
    carlo_garden.print_stat()
    carlo_garden.grow_plants()


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    main()
