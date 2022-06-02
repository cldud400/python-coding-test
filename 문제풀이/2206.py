import sys
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m = map(int,(input().split()))
a = [list(map(int,list(input()))) for _ in range(n)]
dist = [[[0] * 2 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0,0,0))
dist[0][0][0] = 1

while q:
    i, j, k = q.popleft()
    for xy in range(4):
        ni, nj = i + di[xy], j + dj[xy]
        if 0 <= ni < n and 0 <= nj < m:
            # 벽이 아니고 벽을 뚫은 적이 없다면
            if a[ni][nj] == 0 and dist[ni][nj][k] == 0:
                dist[ni][nj][k] = dist[i][j][k] + 1
                q.append((ni,nj,k))
            
            # 벽인데 벽을 뚫은 적이 없다면
            if k == 0 and a[ni][nj] == 1 and dist[ni][nj][k+1] == 0:
                dist[ni][nj][k+1] = dist[i][j][k] + 1
                q.append((ni,nj,k+1))


if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0:
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0:
    print(dist[n-1][m-1][1])
else:
    print(-1)