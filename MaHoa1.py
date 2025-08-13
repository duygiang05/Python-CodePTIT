t = int(input())
for i in range(t) :
    s = input()
    cnt , tmp , ans = 1, s[0], ""
    for j in range(1,len(s)):
        if s[j] != tmp :
            ans += str(cnt) + tmp
            cnt , tmp = 1 , s[j]
        else : cnt += 1
    ans += str(cnt) + tmp
    print(ans)
    