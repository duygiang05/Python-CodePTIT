a = []
while len(a) < 10 :
    a.extend(map(int,input().split()))
s = set()
for i in range(len(a)) :
    s.add(a[i] % 42)
print(len(s))