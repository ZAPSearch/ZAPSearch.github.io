###################################################################
# Question 1
###################################################################
def lbs2kg(lbs):
    kg=2.20462262184878*lbs
    return kg
###################################################################
# Question 2
###################################################################
def id_formater(fn, ln, appelation, city, year):
    print("{2}. {0}, {1} ({3}, {4})".format(fn, ln, appelation, city, year))
###################################################################
# Question 3
###################################################################

###################################################################
# Question 4
###################################################################
def id_formater_display():
    fn=input("What is your first name?")
    ln=input("What is your last name?")
    appelation=input("What is your appellation?")
    city=input("Where were you born?")
    year=input("What is your year of birth?")
    id_formater(fn, ln, appelation, city, year)
###################################################################
# Question 5
###################################################################
def l2loz(w):
    l=w//1
    o=(w%1)*16
    return (l,o)
###################################################################
# Question 6
###################################################################
def draw_soccer_field():
    import turtle
    s=turtle.Screen()
    t=turtle.Turtle()
    t.penup()
    t.goto(-300,96)
    t.pendown()
    t.goto(300,96)
    t.goto(300,-96)
    t.goto(-300,-96)
    t.goto(-300,96)

    t.penup()
    t.goto(0,-28.5)
    t.pendown()
    t.circle(28.5)

    t.penup()
    t.goto(300,60.45)
    t.pendown()
    t.goto(250.5,60.45)
    t.goto(250.5,-60.45)
    t.goto(250.5,-60.45)
    t.goto(300,-60.45)

    t.penup()
    t.goto(-300,60.45)
    t.pendown()
    t.goto(-250.5,60.45)
    t.goto(-250.5,-60.45)
    t.goto(-300,-60.45)


    t.penup()
    t.goto(0,96)
    t.pendown()
    t.goto(0,-96)

    t.penup()
    t.goto(300,20.15)
    t.pendown()
    t.goto(283.5,20.15)
    t.goto(283.5,-20.15)
    t.goto(300,-20.15)

    t.penup()
    t.goto(250.5,-20.15)
    t.pendown()
    t.circle(20.15,-180)

    t.penup()
    t.goto(-300,20.15)
    t.pendown()
    t.goto(-283.5,20.15)
    t.goto(-283.5,-20.15)
    t.goto(-300,-20.15)

    t.penup()
    t.goto(-250.5,20.15)
    t.pendown()
    t.circle(20.15,-180)

    t.penup()
    t.goto(-300,93)
    t.pendown()
    t.circle(3,90)
###################################################################
# Question 7
###################################################################
def median3(num1,num2,num3):
    if num3<num1<num2 or num2<num1<num3:
        print(num1, " is a median.  That is True")
        print(num2, " is a median.  That is False")
        print(num3, " is a median.  That is False")
    elif num3<num2<num1 or num1<num2<num3 :
        print (num1, " is a median.  That is False")
        print (num2, " is a median.  That is True")
        print (num3, " is a median.  That is False")
    elif num1<num3<num2 or num2<num3<num1:
        print (num1, " is a median.  That is False")
        print (num2, " is a median.  That is False")
        print (num3, " is a median.  That is True")
    elif num1==num2:
        print (num1, " is a median.  That is True")
        print (num2, " is a median.  That is True")
        print (num3, " is a median.  That is False")
    elif num2==num3:
        print (num1, " is a median.  That is False")
        print (num2, " is a median.  That is True")
        print (num3, " is a median.  That is True")
    elif  num1==num3:
        print (num1, " is a median.  That is True")
        print (num2, " is a median.  That is False")
        print (num3, " is a median.  That is True")
###################################################################
# Question 8
###################################################################
import math
def below_parabola(a,b,p,q):
    y=a*p**2+b
    if p<a and  q<y or q==y:
        print ('true')
    if p>a or q>y:
        print('false')
###################################################################
# Question 9
###################################################################
def projected_grade(a1,A1,a2,A2,m,M):
    As1=(a1/A1)*5
    As2=(a2/A2)*5
    As3=(((a1/A1)+(a2/A2))/2)*5

    Midterm=(m/M)*35
    Final=(m/M)*50

    score=As1+As2+As3+Midterm+Final
    
    return(score)
###################################################################
# Question 10
###################################################################

###################################################################
# Question 11
###################################################################
def change_to_coins(amount):
    q=amount//0.25
    amount=round(amount%0.25,2)
    d=amount//0.10
    amount=round(amount%0.10,2)
    n=amount//0.05
    amount=round(amount%0.05,2)
    p=amount//0.01
    return(q,d,n,p)
