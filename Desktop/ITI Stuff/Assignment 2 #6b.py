def stats_v2(n):
    import random
    print ("The minimum and the average of the following numbers is:")
    total = 0
    minimum = 100
    for i in range (0,n):
        m = random.randint(-100,100)
        print (m, end = " ")
        total = total + m
        if m < minimum:
            minimum = m
        else:
            minimum = minimum
    average = round((total/n), 2)
    print("\n is", minimum, "and", average)
