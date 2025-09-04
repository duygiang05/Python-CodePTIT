while (n := int(input())) != 0 :
    cnt = 1
    while(n != 1) :
        cnt += 1
        if n % 2 : n = n * 3 + 1
        else : n //= 2
    print(cnt);