#!/usr/bin/env python3
class GardenManager():
    garden_list = []

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name

    @classmethod
    def create_garden_newtwork(cls, gardener_name: str) -> None:
        cls.garden_list.append(cls(gardener_name.capitalize()))

    @staticmethod
    def print_garden(cls) -> None:
        for garden in cls.garden_list:
            print(f"{garden.owner_name}")


class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int) -> None:
        super().__init__(name, height, age)

    @staticmethod
    def is_bloom(self) -> str:
        return ("(blooming!)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 prize_points: int) -> None:
        super().__init__(name, height, age)
        self.prize_points = prize_points


def main():
    GardenManager.create_garden_newtwork("garden1")
    GardenManager.create_garden_newtwork("garden2")
    GardenManager.print_garden(GardenManager)



if __name__ == "__main__":
    main()
