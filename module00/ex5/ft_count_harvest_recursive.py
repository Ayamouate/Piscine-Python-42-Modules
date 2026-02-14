def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    def count_helper(x):
        if (x <= 0):
            return
        count_helper(x - 1)
        print("Day", x)
    count_helper(x)
    print("Harvest time!")
