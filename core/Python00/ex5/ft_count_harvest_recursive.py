def ft_count_harvest_recursive() -> None:
    total_days = int(input("Days until harvest: "))

    def ft_counting_days(current_day) -> None:
        if (current_day > total_days):
            print("Harvest time!")
        else:
            print("Day", current_day)
            ft_counting_days(current_day + 1)
    ft_counting_days(1)


# if __name__ == "__main__":
#    ft_count_harvest_recursive()
