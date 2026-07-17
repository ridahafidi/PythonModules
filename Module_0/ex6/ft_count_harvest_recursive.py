
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    i = 1
    def countdown(days, i):
        if days <= 0:
            print("Harvest time !")
            return
        else:
            print(f"day {i}")
            days -= 1
            i += 1
            countdown(days, i)
    countdown(days, i)
