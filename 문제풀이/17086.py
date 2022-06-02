from collections import deque

di = [0,0,1,-1,1,-1,1,-1]
dj = [1,-1,0,0,1,-1,-1,1]
n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

def solve(x,y):
    d = [[-1] * m for _ in range(n)]
    d[x][y] = 0
    q = deque()
    q.append((x,y))
    while q:
        i, j = q.popleft()
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if d[ni][nj] == -1:
                    if a[ni][nj] == 1: return (d[i][j]+1)
                    else:
                        q.append((ni,nj))
                        d[ni][nj] = d[i][j] + 1

ans = 0
dist = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            dist = solve(i,j)
            if ans < dist:
                ans = dist

print(ans)