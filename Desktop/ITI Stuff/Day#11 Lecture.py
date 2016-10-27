' a quiz game ' 
lines = open('quiz.csv', encoding= "utf-8").read().splitlines()
import random
import time

   
def raw_read_answer():
    ans = 0
    try:
        ans = int(input("Give me a number between 1 - 4:"))
    except ValueError:
        print("Please enter an integer:")
    except:
        print("We don't know whats wrong, but please try again."
    return ans

def read_answer():
    ans = raw_read_answer()
    while ans not in [1,2,3,4]:
        print("Invalid input. Please Try again, please.")
        ans = raw_read_answer()
    return ans
 
def ask_question(q):
    print(q[0])
    for i in range (1,5):
        print (i, q[i])

def play_game():
    questions = []
    for x in lines:
        questions.append(x.split('/t'))

    lives = 3
    while lives > 0:
        q = random.choice(questions)
        ask_question()
        raw_read_answer()
        read_answer()
        score = 0
        answer = 0
        if answer == 1:
            print ("Nice! You got the right answer!")
            score = score + int(q[-1])
        else:
            print("Sorry you got the wrong answer. The right answer is", questions[0][1])
            lives = lives - 1#This is true if the element of a list is another list

play_game()    
