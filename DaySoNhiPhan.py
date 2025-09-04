n = int(input())
a = list(map(int,input().split()))
l , cnt = 1, 0
while l < n :
    if a[l] - a[l - 1] : cnt += 1
    l += 1
print(cnt)