import random
def guessing_game():
    ''' () --> None '''
    print("I am thinking of a number in the set 1,2,3,..1000")
    x = random.randint(1,1000)
    user_input = -1
    tries = 10
    while tries > 0 and user_input != x:
        user_input = int(input("What is your first guess, player?"))
        tries = tries - 1
        if user_input < x:
            print("Ops! Too low! Try again!", "Guesses left =", tries)
        elif user_input > x:
            print("Ops! Too high! Try again, if you want to win!", "Guesses left=", tries)
    if user_input == x:
        print (user_input, "is the right number!", "Guesses left =", tries)
    else:
        print("Sorry try again please!", "The correct number was:", x)

#main
# This function call actually runs the code guessing_game()    

def duplicates(list):
    ''' (list)--> bool
    true if there are duplicates
    false if there arent any dupicates '''
    for i in range(0,len(list)):
        #l[i]
        for j in range (i+1, len(list)):
            if list[i] == list [j]:
                return True
    return False

def duplicates_1(l):
    ''' Same function, but you pick a card and compare it to all cards'''
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] == l[j] and i!= j:
                return True
    return False

#^ the code above is being run [len(l)]^2 times

def duplicates_via_sort():
    
