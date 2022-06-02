n, k = map(int,input().split())
a = [[0] * n for _ in range(2)]
d = [[0]*(k+1) for _ in range(n+1)]
for i in range(n):
    a[0][i], a[1][i] = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, k+1):
        if a[0][i-1] <= j:
            d[i][j] = max(a[1][i-1]+d[i-1][j-a[0][i-1]],d[i-1][j])
        else:
            d[i][j] = d[i-1][j]     
  
print(d[n][k])