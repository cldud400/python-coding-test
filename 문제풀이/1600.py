import sys
from collections import deque

t = int(input())
m, n= map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dist = [[[-1] * (t+1) for _ in range(m)] for _ in range(n)]


di = [0,0,1,-1,-2,-1,1,2,2,1,-1,-2]
dj = [1,-1,0,0,1,2,2,1,-1,-2,-2,-1]
# 나이트 처럼 이동한 횟수와 인접한 방향으로 이동한 횟수
cost = [0,0,0,0,1,1,1,1,1,1,1,1]


dist[0][0][0] = 0
q = deque()
q.append((0,0,0))

while q:
    i, j, z = q.popleft()
    for k in range(12):
        ni, nj, nz = i + di[k], j + dj[k], z + cost[k]
        if 0 <= ni < n and 0 <= nj < m:
            if nz <= t:
                if a[ni][nj] == 1: continue
                if dist[ni][nj][nz] == -1:
                    dist[ni][nj][nz] = dist[i][j][z] + 1
                    q.append((ni,nj,nz))
        

    
ans = -1
for c in range(t+1):
    if dist[n-1][m-1][c] == -1: continue
    if ans == -1:
        ans = dist[n-1][m-1][c]
    elif ans > dist[n-1][m-1][c]:
        ans = dist[n-1][m-1][c]

print(ans)

