#while boolean_expression:
 #   statement(s)

'''answer = input("Do you want to buy a plane ticket?")
while not(answer.strip().lower() == "Yes" or answer.strip().lower() == "NO"):
    print("invalid input")
    answer = input("Do you want to buy a plane ticket?")'''

def print_until_vowel(s):
    i = 0
    while i < len(s) and s[i] not in 'aeiouAEIOU':
        print(s[i])
        i=i+1
#make sure that i < len(s) is a head of "s[i] not in 'aeiouAEIOU' becuase s[3] not being present is gonna cause it to crash

def collatz(n):
    while n != 1:
        if n%2 == 0:
           n = n//2
        else:
           n = 3*n + 1
        return (n)
    return ("True")
    
n = 1
while n <= 1000:
    collatz(n)
    n = n+1
