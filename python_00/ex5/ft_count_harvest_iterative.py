def ft_count_harvest_iterative():
    given_number = int(input("Days until harvest: "))
    i = 1
    for i in range(1, given_number + 1):
        print(f"Day {i}")
    print("Harvest time!")
