t = int(input())

for _ in range(t) :
    s = input()
    n = input()
    # l = len(n) ; cnt = 0
    # while l <= len(s) :
    #     tmp = l - len(n)
    #     if s[tmp : l] == n : 
    #         cnt += 1
    #         l += len(n)
    #     else : l += 1
    # print(cnt)
    print(s.count(n))