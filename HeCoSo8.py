s = input()

while len(s) % 3 :
    s = '0' + s

for i in range(0,len(s) - 3 + 1,3) :
    ss = s[i:i + 3]
    print(int(ss,2),end='')
