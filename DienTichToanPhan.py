t = int(input())
matrix = []

for i in range(t) :
    matrix.clear()
    m,n = map(int,input().split())
    
    for i in range(m) :
        row = list(map(int,input().split()))
        matrix.append(row)
    
    day,trai,phai,tren , duoi = 0,0,0,0,0
    for i in range(m) :
        for j in range(n) :
            tmp = matrix[i][j]
            if tmp : day += 1
            trai += tmp ; phai += tmp ; tren += tmp; duoi += tmp
            if j > 0 : trai -= min(tmp,matrix[i][j - 1])
            if i > 0 : tren -= min(tmp,matrix[i - 1][j])
            if j < n - 1 : phai -= min(tmp,matrix[i][j + 1])
            if i < m - 1 : duoi -= min(tmp,matrix[i + 1][j])
    
    print(day * 2 + tren + duoi + trai + phai) 
    