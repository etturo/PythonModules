#!/usr/bin/env python3
import sys


def main() -> None:
    inventory: dict = {}
    for arg in sys.argv[1:]:
        try:
            item, quantity = arg.split(":")
            inventory[item] = int(quantity)
        except ValueError as e:
            print(f"Error: {e}")
            return
    total_items = 0
    for key in inventory.keys():
        total_items += inventory[key]
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item type: {len(inventory)}")
    print()
    print("=== Current Inventory ===")
    for key in inventory.keys():
        print(f"{key}: {inventory[key]} units "
              f"({(inventory[key] / total_items * 100):.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    max_item: int = 0
    max_key: str = ""
    for key in inventory.keys():
        if max_item < inventory[key]:
            max_item = inventory[key]
            max_key = key
    print(f"Most aboundant: {max_key} ({max_item} units)")
    min_item: int = max_item
    for key in inventory.keys():
        if min_item > inventory[key]:
            min_item = inventory[key]
            min_key = key
    print(f"Least aboundant: {min_key} ({min_item} units)")
    print()
    print("=== Item Categories ===")
    categories: dict = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {}
    }
    for key, value in inventory.items():
        if value >= 5:
            categories["Abundant"][key] = value
        elif value >= 3:
            categories["Moderate"][key] = value
        else:
            categories["Scarce"][key] = value
    for category, item in categories.items():
        if item:
            print(f"{category}: {item}")
    print()
    print("=== Management Suggestions ===")
    print("Restock Needed: [", end="")
    first: bool = True
    for key, value in inventory.items():
        if value == 1:
            if first is False:
                print(", ", end="")
            print(f"'{key}'", end="")
            first = False
    print("]\n")
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:   [", end="")
    first = True
    for key in inventory.keys():
        if first is False:
            print(", ", end="")
        print(f"'{key}'", end="")
        first = False
    print("]")
    print("Dictionary values:   [", end="")
    first = True
    for values in inventory.values():
        if first is False:
            print(", ", end="")
        print(f"{values}", end="")
        first = False
    print("]")
    print("Sample lookup - 'sword' in inventory: "
          f"{bool(inventory.get('sword'))}")


if __name__ == "__main__":
    print("\n=== Inventory System Analysis ===\n")
    main()
    print()
