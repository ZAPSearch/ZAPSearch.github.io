#Question2
def two_length_run(l):
    try:
        for i in range(len(l)-2):
            if l[i] == l[i+1]:
                return True
        return False
    except:
        return False

s = input("Please input a list of numbers separated by commas: ")
try:
    l = list(eval(s))
except:
    l = 0
print (two_length_run(l))
