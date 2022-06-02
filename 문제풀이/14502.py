import sys
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m = map(int, input().split())
ans = 0
a = []
for i in range(n):
    a.append(list((map(int, input().split()))))



def bfs(a):
    n = len(a)
    m = len(a[0])
    b = [[0] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
            if b[i][j] == 2:
                q.append((i,j))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and b[ni][nj] == 0:
                b[ni][nj] = 2
                q.append((ni,nj))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0: cnt += 1

    return cnt


#첫번째 벽
for x1 in range(n):
    for y1 in range(m):
        if a[x1][y1] != 0: continue
        
        # 두번째 벽
        for x2 in range(n):
            for y2 in range(m):
                if a[x2][y2] != 0: continue
                
                # 세번째 벽
                for x3 in range(n):
                    for y3 in range(m):
                        if a[x3][y3] != 0: continue
                        

                        # 같은 위치에 벽 X
                        if x1 == x2 and y1 == y2: continue
                        if x2 == x3 and y2 == y3: continue
                        if x3 == x1 and y3 == y1: continue

                        # 벽을 세우고
                        a[x1][y1] = 1
                        a[x2][y2] = 1
                        a[x3][y3] = 1

                        # BFS | DFS
                        ret = bfs(a)
                        if ans < ret:
                            ans = ret

                        # 벽을 원복
                        a[x1][y1] = 0
                        a[x2][y2] = 0
                        a[x3][y3] = 0
print(ans)