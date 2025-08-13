def chen(x) :
    cnt, ans = 0, ""
    for i in range(len(x) - 1, -1, -1) :
        cnt += 1
        ans = x[i] + ans
        if cnt == 3 and i != 0:
            cnt = 0
            ans = "," + ans
    return ans

n = input()
print(chen(n))
 

