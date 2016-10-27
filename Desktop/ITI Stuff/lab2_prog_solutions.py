#Excercise_1
def repeater(s1, s2, n):
    '" (String, String, Integer) --> (String)/n Two forms of string are given by the user and they are repeated a certain number of times (also given by the user)."'
    result = "_" + (s1 + s2)*n + "_"
    return (str(result))

    
#Excercise_2
import math
def roots(a,b,c):
    '" (Float, Float, Float) --> (Float, Float)/n User enters coefficients to a function and the function finds the roots of said function."'
    root1 = (-(b) + math.sqrt((b**2) - (4*a*c)))/(2*a)
    root2 = (-b - math.sqrt((b**2) - (4*a*c)))/(2*a)
    print("The quadratic function with coefficients a =", a, "b =", b, "c=", c,"/n has the following roots:", root1, "and", root2)

#Excercise_3
import math
def real_roots(a, b, c):
    '" (Float, Float, Float) --> (Float, Float)/n User enters coefficients to a function and the function states if function is factorable or not"'
    discriminant = 0
    value = (discriminant < ((b**2) - (4*a*c)))
    return (value)


#Excercise_4
def reverse(number):
    '" (Integer) --> (Integer) This function reverses the order of any two-dgit integer inserted into the function."'
    digit_one = str(number%10)
    digit_two= str(number//10)
    print (digit_one+digit_two)


