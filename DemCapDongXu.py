n = int(input())

a = []

for i in range(n) :
    s = input()
    a.append(s)

cnt = 0

for i in range(n) :
    for j in range(n) :
        if a[i][j] == 'C' :
            for k in range(j + 1,n) : 
                if a[i][k] == 'C' : cnt += 1

for i in range(n) :
    for j in range(n) :
        if a[i][j] == 'C' :
            for k in range(i + 1,n) :
                if a[k][j] == 'C' : cnt += 1
                
print(cnt)