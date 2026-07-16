def ft_harvest_total():
    harvest_total = 0
    for day in range(1,4):
        harvest_total += int(input(f"day {day} harvest: "))
    print(f"Total harvest: {harvest_total}")
    