t = int(input())

for i in range(t) :
    n = input()
    sum , mul , check = 0 ,1, False
    for i in range(len(n)) :
        if not i % 2 :
            if int(n[i]) : 
                mul *= int(n[i])
                check = True
        else : sum += int(n[i]);
    mul = 0 if not check else mul
    print(mul,sum, sep=' ')