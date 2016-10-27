#Programming Excercise 1
def sum_odd_while_v2(n):
    total = 0
    i = 5
    while i <= n and i%2 != 0:
        total = total + i
        i += 2
    return (total)

#Programming Excercise 2
def do_you_want_to_add():
    answer = input("Do you want to add the two numbers of your choice?")
    while answer == "yes":
        int_1 = int(input("What is your first integer?"))
        int_2 = int(input("What is your second integer?"))
        sum = int_1 + int_2
        print (sum)
        answer = input("Do you want to add the two numbers of your choice?")

#Programming Excercise 3
def first_neg(l):
    i = 0
    if len(l) == 0:
        return None
    while l[i] > 0:
        if i == len(l):
            return None
        i = i + 1
    return (i)

#Programming Excercise 4a
def sum_5_consecutive(l):
    i = 0
    while 5+i <= len(l):
        h = l[0+i:5+i]
        i = i +1
        if sum (h) == 0:
            return True
        
    return False

#Programming Excercise 4b
def sum_5_consecutive_for(l):
    if len(l) >= 5:
        for i in range (0, len(l)):
            z = l[i:5+i]
            if sum(z) == 0:
                return True
    return False

#Programming Excercise 5
#Programming Excercise 6
def fib(n):
    z = []
    z.append(1)
    z.append(1)
    for i in range(2,n):
        z.append((z[i-1] + z[i-2]))
    print (z)
#Programming Excercise 7
def inner_product(s,t):
    x =[]
    for i in range(0,len(s)):
        y = s[i] * t[i]
        x.append(y)
    print (sum(x)) 
