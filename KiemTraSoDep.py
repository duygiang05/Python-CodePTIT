def check(s) :
    for i in range(2,len(s)) :
        if s[i] != s[i - 2] : return False
    return True
 
t = int(input())

for i in range(t) :
    s = input()
    if len(set(s)) == 2 and check(s) : print("YES")
    else : print("NO")
    