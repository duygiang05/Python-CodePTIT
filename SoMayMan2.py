def check(x) :
    for i in x :
        if i != "4" and i != "7" :
            return False

    return True

t = int(input())

for i in range(t) :
    n = input()
    
    if check(n) == True : 
        print("YES")
    else :
        print("NO")