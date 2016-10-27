import random
def ah(l,x,y):
    z=[]
    for i in l:
        if i < y and i > x:
           z.append(i)
    h = min(z)
    return (len(z),h)

def is_perfect(n):
    z = 0
    for i in range (1,n):
        if (n%i) == 0:
            z = z +i
        else:
            z = z +0
    if z == n:
        return True
    else:
        return False

for i in range(0,35000000):
    z = is_perfect(i)
    if z == True:
        print(i)

 
def arithmetic(z):
    h = []
    t = []
    for i in range(0, len(z)) and x in range (1, len(z)+1):
       diff = z[len(z)-i] - z[len(z)-x]
       h.append(diff)

    for r in range (0,len(h)) and m in range (1, len(h)+1):
        diffe = h[len(h)-r] - h[len()-m] 
        z.append(diffe)
    if h == t:
        return True
    else:
        return False 
    
