def checkTang(x) :
    for i in range(1,len(x)) :
        if x[i] <= x[i - 1] : return False
    return True

def checkGiam(x) :
    for i in range(1,len(x)) :
        if x[i] >= x[i - 1] : return False
    return True

def checkAll(x) :
    for i in range(1,len(x)) :
        if checkTang(x[:i]) and checkGiam(x[i:]) : return True
    return False
    

t = int(input())

for _ in range(t) :
    n = input()
    if len(n) < 3 : print("NO")
    else :
        if checkAll(n) : print("YES")
        else : print("NO")