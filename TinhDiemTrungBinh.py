n = int(input())

a = list(map(float,input().split()))

mx = max(a); mn = min(a); ans = 0.0 ; cnt = 0

for x in a : 
    if x != mx and x != mn : 
        ans += x; cnt += 1
print("%.2f" % (ans / float(cnt)))