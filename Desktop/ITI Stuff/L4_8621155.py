#Task_1
s1 = "good"
s2 = "bad"
s3 = "silly"
str.strip(s1)

#Programming_exercise_1
def is_eligible(a, c, p):
    c = c.lower()
    c = c.strip()
    p = p.lower()
    if c == "canadian" or c == "canada" and a > 18 and p == "no":
        print("According to Canadian rules and regulations, you are eligible to vote.")
    else:
        print("According to Canadian rules and regulations, you are not eligible to vote.")
        
#Programming_Excercise_2
def mess(s):
    for i in ["r", "s", "t", "v", "w", "x","y" , "z"]:
        if i in s:
            s = s.replace (i, i.upper())
           
    print(s)
    
def mess2(s):
    z=""
    for i in range(len(s)):
        if s[i] in ["r", "s", "t", "v", "w", "x","y" ,"z"]:
            z = z+ s[i].upper()
        elif s[i] == " ":
            z = z + "-"
        else:
            z = z + s[i]
    print (z)




        
#Programming_Excercise_3
def print_all_23n8(num):
    for i in range(num):
        if i % 2 is 0 or i%3 == 0 and i%8 != 0:
            print (i)
num = int(input("What is the given number?"))
n = print_all_23n8(num)
print (n)

#Programming_Excercise_4
def draw(num):
 for i in range (num):
    print(i*"$")    

#Programming_Excercise_5
num = int(input("Enter your positive number here:"))
for i in range (1, num+1):
    t = num%i
    if t == 0:
        print (i)
       
def prime(num):
    if num == 1:
          return True
    elif num == 0:
          return False
    else:
        for i in range(2 , num): 
            z = num%i
            if z == 0:
                return False
            else:
                return True
   
        
        
        
