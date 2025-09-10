n = int(input())

a = list(map(int,input().split()))
a.sort()

a1 = a[n-1]; a2 = a[n-2]; a3 = a[n-3] ; a4 = a[0] ; a5 = a[1]

print(max(a1*a2*a3 , a1*a2, a1 * a4 * a5, a1 * a4 * a5))