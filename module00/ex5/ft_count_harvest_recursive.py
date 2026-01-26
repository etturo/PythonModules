#!/usr/bin/env python3
def ft_count_harvest_recursive():
    def ft_count_harvest_recursive_helper(days):
        if days == 0:
            return
        ft_count_harvest_recursive_helper(days - 1)
        print(f"Day {days}")
        return
    print("Days until harvest: ", end="")
    days = int(input())
    ft_count_harvest_recursive_helper(days)
    print("Harvest time!")


# if __name__ == "__main__":
#     ft_count_harvest_recursive()
