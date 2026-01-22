def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds:",
              f"covers {quantity} square meters")
    else:
        print("Unknown unit type")


# def main():
#     ft_seed_inventory("TOMATO", 15, "packets")
#     ft_seed_inventory("carrot", 8, "grams")
#     ft_seed_inventory("LATTUCE", 12, "area")
#     ft_seed_inventory("tomato", 15, "ASDRUBALE")


# if __name__ == "__main__":
#     main()
