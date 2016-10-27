#Question3
def two_length_run(l):
    z = 1
    try:
        l.sort()
        for i in range(len(l)-2):
            if l[i] == l[i+1]:
                z = z + 1
            elif l[i] != l[i+1]:
                
        return max()
    except:
        return 0

s = input("Please input a list of numbers separated by commas: ")
try:
    l = list(eval(s))
except:
    l = 0
print (two_length_run(l))
