def check(s) :
    for i in range(2,len(s),2):
        if s[i] != s[i - 2] : return False
    return True

t = int(input()) 

for i in range(t) :
    s = input()
    if check(s) and len(s) % 2 and s[0] != s[1] : print("YES")
    else : print("NO")