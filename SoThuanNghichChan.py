def check(x) :
    for i in x :
        if int(i) % 2 == 1 :
            return False
    return True



t = int(input()) 
for i in range (t) :
    n = int(input())
    for i in range (22,n,2) :
        x = str(i)
        if x != x[::-1] : continue
        if len(x) % 2 == 1 : continue
        if not check(x) : continue
        print(i, end = ' ')
    print()