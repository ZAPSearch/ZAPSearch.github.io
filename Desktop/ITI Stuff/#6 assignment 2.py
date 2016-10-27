#Question6b
def stats_v2(n):
    import random
    z = 0
    print("The minimum and the average of the following numbers:\n"
    for i in range (0,n):
        z = random.randint(range(-100,100))
        z = z
        for i in random.sample(range(-100,100),n):
            total = total + i
            print(i, new = " ")
                if z[i]<z[i-1] :
                  m = i 
    print ("\n are", m, "and", (total/n)))

#Question5
def vote():
    user_input = input("Enter the yes, no, abstained votes one by one and then press enter:")
    user_input = user_input.strip().lower()
    positive = user_input.count('y')
    negative = user_input.count('no')
    total = negative + positive
    percentage = ((positive/total)*100)
    if percentage == 100:
        print("Proposal passes unanimously")
    elif percentage >= 75:
        print ("Proposal passes with super majority")
    elif percentage >= 50:
        print ("Proposal passes with simple majority")
    else:
        print ("Proposal fails")


