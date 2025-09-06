t = int(input())

for _ in range(1,t + 1) :
    s1 = input()
    s2 = input()
    d1 = {} ; d2 = {}
    
    for h in s1 :
        d1[h] = d1.get(h,0) + 1
    
    for h in s2 :
        d2[h] = d2.get(h,0) + 1
        
    if len(s1) != len(s2) : print(f"Test {_}: NO")
    else :
        check = True
        for x,y in d2.items() :
            tmp = d1.get(x,0)
            if tmp != y :
                print(f"Test {_}: NO"); check = False ; break
                
        if check : print(f"Test {_}: YES")