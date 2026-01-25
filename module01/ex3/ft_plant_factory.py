#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.initial_height: int = height
        self.initial_age: int = age
        print(f"Created: {self.name.capitalize()}"
              f"({self.height}cm, {self.age} days)")


def main():
    plants = []
    plants.append(Plant("rose", 25, 30))
    plants.append(Plant("oak", 200, 365))
    plants.append(Plant("oak", 5, 90))
    plants.append(Plant("sunflower", 80, 45))
    plants.append(Plant("fern", 15, 120))
    i = 0
    for plant in plants:
        i += 1
    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    main()
