import sys
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m, t = map(int,(input().split()))
a = [list(map(int,list(input()))) for _ in range(n)]
dist = [[[[0] * 2] * (t+1) for _ in range(m)] for _ in range(n)]


q = deque()
q.append((0,0,0,0))
dist[0][0][0][0] = 1



while q:
    i, j, k, l = q.popleft()
    for xy in range(4):
        ni, nj = i + di[xy], j + dj[xy]
        if 0 <= ni < n and 0 <= nj < m:
            if a[ni][nj] == 0 and dist[ni][nj][k][1-l] == 0:
                dist[ni][nj][k][1-l] = dist[i][j][k][l] + 1
                q.append((ni,nj,k,1-l))


            if l == 0 and k+1 <= t and a[ni][nj] == 1 and dist[ni][nj][k+1][1-l] == 0:
                dist[ni][nj][k+1][1-l] = dist[i][j][k][l] + 1
                q.append((ni,nj,k+1,1-l))


        if dist[i][j][k][1-l] == 0:
            dist[i][j][k][1-l] = dist[i][j][k][l] + 1
            q.append((i,j,k,1-l))

ans = -1
for d in range(2):
    for c in range(t+1):
        if dist[n-1][m-1][c][d] == 0: continue
        if ans == -1:
            ans = dist[n-1][m-1][c][d]
        elif ans > dist[n-1][m-1][c][d]:
            ans = dist[n-1][m-1][c][d]


print(ans)