t = int(input())
for i in range(t) :
    s = input()
    tmp , ans , cnt = "", "" , 0
    for x in s :
        if x.isdigit() == True :
            cnt = int(x)
            ans += (tmp * cnt)
        else :
            tmp = x 
    print(ans)