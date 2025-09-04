t = int(input())
a = []
l = 1 ; a.extend([0,1])

while l < 94 :
    a.append(a[l] + a[l - 1])
    l += 1
    
for i in range(t) :
    c,b = map(int,input().split())
    for h in a[c:b + 1] :
        print(h,end=' ')
    print()
        
    