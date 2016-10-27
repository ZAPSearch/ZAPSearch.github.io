#Name : Zaid Saeed
#Student Number : 8621155
# Assignment Number 2
import random
#######Question1####
def size_format(i):
    ''' (Int) --> (Int)
This function takes the number of bytes inputted by the user and tells him/her how many metric units of bytes s/he has (mega,tera, kilo, etc)'''
    if i<0:
        print("Buy a new hard disk")
    elif i < 1000:
        print(i, "B")
    elif i > 1000 and i < (1000**2):
        i = round(i/1000, 1)
        print (i, "KB")
    elif i > (1000**2) and i < (1000**3):
        i = round(i/(1000**2), 1)
        print(i, "MB")
    elif i > (1000**3) and i < (1000**4):
        i = round(i / (1000**3), 1)
        print(i, "GB")
    elif i > (1000**4):
        i = round(i / (1000**4), 1)
        print (i, "terabytes")
#######Question2####
def add_article(s):
    ''' (string) --> (string) This function takes in a country's name and adds an article to that country's name depending on whether the country's name is masculine, feminine or plural '''
    if s == "Belize" or s == "Cambodge" or s == "Mexique" or s=="Mozambique" or s == "Zaire" or s=="Zimbabwe":
        print ("le", s)
    elif s[0] in 'aeiouAEIOU':
        print ("l'"+s)
    elif s[len(s)- 1] == "e":
        print ("la",s)
    elif s == "Etats-Uni" or s == "Pay-Bas":
        print ("les",s)
    else:
        print("le",s)
#######Question3####
def factorial(n):
    ''' (Integer) --> (Integer) This function asks the user for a number as an input and gives him the factorial of that function as an output.'''
    z = []
    y = []
    f = 1
    if n == 0:
        print (1)
    else:
        for i in range(0,n-1):
            z.append(i)
            h = n-z[i]
            y.append(h)
        for i in range (0, len(y)):
            f = f*y[i] 
        print (f)
#######Question4####
def special_count(l):
    ''' ''' 
    counter = 0
    for i in range (0, len(l)):
        z = l[i]
        if z >= 0 and z%4 == 0 and not(z % 100 == 0 and z % 400 != 0):
            counter = counter + 1
    print (counter)

