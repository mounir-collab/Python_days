def ft_count_harvest_recursive():
    given_number = int(input("Days until harvest: "))

    def repeat(day):
        if day > given_number:
            print("Harvest time!")
            return
        print(f"Day {day}")
        repeat(day + 1)
    repeat(1)
