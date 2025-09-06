t = int(input())

for _ in range(t) :

    s = input()
    sum = 0

    tmp = ''

    for h in s :
        if h.isdigit() :
            sum += int(h)
        else : tmp += h
        
    a = list(tmp); a.sort()

    for i in a : print(i,sep='',end='')
    print(sum)