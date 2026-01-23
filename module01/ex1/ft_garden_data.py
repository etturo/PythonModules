#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def return_stats(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(rose.return_stats())
    print(sunflower.return_stats())
    print(cactus.return_stats())


if __name__ == "__main__":
    main()
