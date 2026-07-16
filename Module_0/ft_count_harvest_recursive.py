def ft_count_harvest_recursive():
    # days = 1
    #days = int(input("Days until harvest: "))
    if days <= 0:
        print("Harvest time !")
        return
    else:
        print(f"day {days}")
        days -= 1
        ft_count_harvest_recursive()
    