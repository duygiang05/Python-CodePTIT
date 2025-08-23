def coso3(ch) :
    return ch in '012'

def check(s) :
    for i in s :
        if not coso3(i) : return False
    return True

t = int(input()) 

for i in range(t) :
    s = input()
    if check(s) : print("YES")
    else : print("NO")