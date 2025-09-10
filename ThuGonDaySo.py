n = int(input())

a = list(map(int,input().split()))
l, cnt = 0, 0
while l < len(a) - 1 :
    if not (a[l] + a[l + 1]) % 2 : 
        cnt += 2 ; l += 2
    else : l += 1

print(len(a) - cnt)

