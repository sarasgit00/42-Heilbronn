def ft_water_reminder() -> None:
    days = int(input("Days since watering: "))
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
