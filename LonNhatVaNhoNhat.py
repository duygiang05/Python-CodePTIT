
while (n := int(input())) != 0 :
    a = []
    
    for i in range(n) :
        s = input()
        a.append(int(s))

    mx = max(a); mn = min(a)
    if(mx == mn) : print("BANG NHAU")
    else : print(mn,mx,sep = ' ')