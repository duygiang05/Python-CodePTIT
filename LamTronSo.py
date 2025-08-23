def change(n) :
    if int(n) < 11 : return n
    nho = 0
    s = ''
    for i in reversed(range(1,len(n))) :
        tmp = int(n[i])
        s = '0' + s
        if tmp + nho >= 5 :
            nho = 1
        else : nho = 0
    s = str(int(n[0]) + nho) + s
    
    return s

t = int(input())

for i in range(t) :
    n = input()
    print(change(n))
    