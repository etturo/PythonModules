#!/usr/bin/env python3
def ft_water_reminder():
    print("Days since last watering: ", end="")
    days = int(input())
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


# if __name__ == "__main__":
#     ft_water_reminder()
