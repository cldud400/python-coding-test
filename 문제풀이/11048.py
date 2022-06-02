n, m = map(int,input().split())

a = [[] for _ in range(n+1)]
a[0] = [0] * (m+1)
for x in range(1,n+1):
    a[x] = [0]+list(map(int,input().split()))

d = [[0]*(m+1) for _ in range(n+1)]



for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = max(d[i-1][j],d[i][j-1],d[i-1][j-1]) + a[i][j]



# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if j + 1 <= m and d[i][j+1] < d[i][j] + a[i][j+1]:
#             d[i][j+1] = d[i][j] + a[i][j+1]
#         if i +1 <= n and [i+1][j] < d[i][j] + a[i+1][j]:
#             d[i+1][j] = d[i][j] + a[i+1][j]
#         if j + 1 <= m and i + 1 <= n and [i+1][j+1] < d[i][j] + a[i+1][j+1]:
#             d[i+1][j+1] = d[i][j] + a[i+1][j+1]

print(d[n][m])