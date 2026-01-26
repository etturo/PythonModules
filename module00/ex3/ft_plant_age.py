#!/usr/bin/env python3
def ft_plant_age():
    print("Enter the age in days: ", end="")
    age = int(input())
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant need more time to grow")


# if __name__ == "__main__":
#     ft_plant_age()
