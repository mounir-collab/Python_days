def ft_harvest_total():
    total = 0
    count = 1
    while count <= 3:
        weight_day = int(input(f"Day {count} harvest: "))
        total += weight_day
        count += 1
    print(f"Total harvest: {total}")
