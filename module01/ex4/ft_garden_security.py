#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self._name.capitalize()}")

    def set_height(self, new_height):
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}"
                  "\t[REJECTED]\n"
                  "Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm	[OK]")

    def get_height(self):
        return self._height

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age}"
                  "\t[REJECTED]\n"
                  "Security: Negative age rejected")
        else:
            self._height = new_age
            print(f"Age updated: {new_age} days	[OK]")

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def get_info(self):
        return (f"{self.get_name().capitalize()}"
                f" ({self.get_height()}cm, {self.get_age()} days)")


def main():
    rose = SecurePlant("rose", 24, 29)
    carrot = SecurePlant("carrot", 13, 12)
    plant_list = []
    plant_list.append(rose)
    plant_list.append(carrot)
    print("\nPLANT STATUS:")
    for plant in plant_list:
        print(f"{plant.get_info()}")
    print("\nCORRECT NEW DATA")
    for plant in plant_list:
        plant.set_height(plant.get_height() + 1)
        plant.set_age(plant.get_age() + 1)
    print("\nPLANT STATUS:")
    for plant in plant_list:
        print(f"{plant.get_info()}")
    print("\nINCORRECT NEW DATA")
    for plant in plant_list:
        plant.set_height(-10)
        plant.set_age(-10)
    print("\nPLANT STATUS:")
    for plant in plant_list:
        print(f"{plant.get_info()}")


if __name__ == "__main__":
    print("=== Garden Security System ===\n")
    main()
    print()
