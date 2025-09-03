import math

T = "0123456789ABCDEF"

t = int(input())

for i in range(t) :
    b = int(input())
    s = input(); 
    x = int(math.log2(b))
    ans = ''
    
    while len(s) % x :
        s = '0' + s
        
    for j in range(0,len(s),x) :
        tmp = s[j : j + x]
        val = int(tmp,2)
        ans += T[val]
    print(ans)
        