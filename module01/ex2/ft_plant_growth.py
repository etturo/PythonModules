#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days
        self.initial_height = height

    def return_stats(self):
        return f"{self.name}: {self.height}cm, {self.days} days old"

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        return (f"{self.name.capitalize()}: "
                f"{self.height}cm, "
                f"{self.days} days old")


def main():
    print("=== Day 1 ===")
    rose = Plant("rose", 25, 30)
    carrot = Plant("carrot", 13, 22)
    print(rose.get_info())
    print(carrot.get_info())
    for i in range(1, 7):
        rose.grow()
        rose.age()
        carrot.grow()
        carrot.age()
    print()
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week of {rose.name.capitalize()} is:",
          f"is +{rose.height - rose.initial_height}cm")
    print()
    print(carrot.get_info())
    print(f"Growth this week of {rose.name.capitalize()} is:",
          f"is +{rose.height - rose.initial_height}cm")


if __name__ == "__main__":
    main()
