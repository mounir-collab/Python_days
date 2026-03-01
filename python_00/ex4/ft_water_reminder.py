def ft_water_reminder():
    count_days = int(input("Days since last watering: "))
    if count_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
