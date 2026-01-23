#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name.capitalize()} (Flower): "
              f"{self.height}cm, {self.age} days, "
              f"{self.color} color")

    def bloom(self):
        print(f"{self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name.capitalize()} (Tree): "
              f"{self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")

    def produce_shade(self):
        print(f"{self.name.capitalize()} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name.capitalize()} (Vegetable): "
              f"{self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")


def main():
    rose = Flower("rose", 25, 30, "red")
    rose.bloom()
    print()
    oak = Tree("oak", 500, 1825, 50)
    oak.produce_shade()
    print()
    tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
    print(f"{tomato.name.capitalize()} is rich in {tomato.nutritional_value}")




if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    main()
    print()
