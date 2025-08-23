def dao(x) :
    s = str(x)
    tmp = int(s[::-1])
    return tmp + x

t = int(input())

for i in range(t) :
    n = int(input())
    check = False
    for j in range(1000) :
        if not n % 7 :
            check = True
            print(n)
            break
        n = dao(n)
    if not check : print(-1)