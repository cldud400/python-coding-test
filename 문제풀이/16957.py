n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

di = [0,1,1,1,0,-1,-1,-1]
dj = [1,1,0,-1,-1,-1,0,1]

ans = [0] * (n*m)
d = [0] * (n*m)


def solve(x):
    if d[x] == x: return x
    else:
        d[x] = solve(d[x])
        return d[x]
    
for i in range(n):
    for j in range(m):
        x, y = i, j
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if a[ni][nj] < a[x][y]:
                    x = ni
                    y = nj
        d[i*m+j] =  x * m + y

for i in range(n):
    for j in range(m):
        ans[solve(i*m+j)] += 1

    

for i in range(n):
    print(*ans[i*m:(i+1)*m])