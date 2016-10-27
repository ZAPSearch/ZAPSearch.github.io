#Question6a
import random
def stats_v1(n):
    total = 0
    z = []
    for i in random.sample(0,n):
        r = random.randint(-100,100)
        z = z.append(r)
        total = total + i
    print ("The minimum and the average of the following numbers:\n", z[:], "\n" ,"are", min(z), "and", (total/n))


#Question7
def emphasize(s):
    ''' This function takes string s an input and returns a string with a blank space inserted between every pair of consecutive characters in s.'''
    for i in range(0,len(s)):
        if s[i] < s[len(s)-1]:
            print(s[i] + " ", end = " ")
        else:
            print (s[i], end = " ")
#Question8
def crypto(s):
    ''' '''
    x = round((len(s))/2)
    if len(s) == 0 or len(s) == 1:
        print(s)
    else:
        for i in range (0, x):
           print(s[(len(s)-1)-i], end = "")
           print(s[i], end = "")
