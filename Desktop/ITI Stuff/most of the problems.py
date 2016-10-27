#Name : Zaid Saeed
#Student Number : 8621155
#Question 1
def size_format(i):
    ''' (Int) --> (Int)
This function takes the number of bytes inputted by the user and tells him/her how many units of bytes s/he has (mega,tera, kilo, etc)'''
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

#Question 2
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



#Question4
''' (list) --> (integer) This function tells you which of the numbers in the entered list is a special number. A special number is one that is non-negative, divisible by four, except that it is not divisible by 100 unless it is also divisible by 400 '''
def special_count(l):
    counter = 0
    for i in range(0, len(l)):
        z = l[i]
        if z >= 0 and z%4 == 0 and not(z % 100 == 0 and z % 400 != 0):
            counter = counter + 1
    print (counter)

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
          
#Question9
def stranger_things(l1,l2):
   ''' (list, list) --> (boolean) This function takes in as input two non-empty lists and compares whether
both lists are of the same length or not, and if that condition is not met, then it compares both lists to see if they have any
elements that are common.
eg) >>> stranger_things([1,2,True, '7'],[1,False,True,5])
True
>>> stranger_things([1,2,3,4],[1,2,3,4])
False
>>> stranger_things([1,2,4],[1,'2',3])
False''''  
    if len(l1) == len(l2):
        for i in range(min(len(l1),len(l2))):
            if l1[i] != l2[i]:       
                return False
            else:
                return True
    else:
        return False
   
