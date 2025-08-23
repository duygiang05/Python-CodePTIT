p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s = input() 
    if s[0] != '0' :
        k , x = s.split()
        tmp = ""
        for i in range(len(x)) :
            ind = p.find(x[i])
            tmp += p[(ind + int(k) ) % 28]
        print(tmp[::-1])
    else : break