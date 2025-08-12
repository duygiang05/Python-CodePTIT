def check(s) :
    for _ in range(1, len(s)) :
        if s[_] < s[_ - 1] : return False
    return True
        
t = int(input())

for _ in range(t) :
    s = input()
    if check(s) == False :
        print("NO")
    else :
        print("YES")
    