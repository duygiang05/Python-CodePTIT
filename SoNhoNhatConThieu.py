n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 1
for x in a:
    if x == ans:
        ans += 1
    elif x > ans:
        break

print(ans)
