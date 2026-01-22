def ft_count_harvest_recursive():
    def ft_count_harvest_recursive_helper(days):
        if days == 0:
            return
        print(f"Day {days}")
        ft_count_harvest_recursive_helper(days - 1)
        return
    print("Days until harvest: ", end="")
    days = int(input())
    ft_count_harvest_recursive_helper(days)
    print("Harvest time!")


# def main():
#     ft_count_harvest_recursive()


# if __name__ == "__main__":
#     main()
