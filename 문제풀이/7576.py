import sys
from collections import deque
# sys.setrecursionlimit(1000000)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m= map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

arr = [[-1]* n for _ in range(m)]
queue = deque()

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            arr[i][j] = 0
            queue.append((i,j))
        # elif tomato[i][j] == 0:
        #     arr[i][j] = 0

def bfs():
    while queue:
        i,j = queue.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < m and 0 <= nj < n:
                if arr[ni][nj] == -1 and tomato[ni][nj] == 0: # 방문한 적이 없고 길이 있을 때
                    queue.append((ni,nj))
                    arr[ni][nj] = arr[i][j] + 1


bfs()

ans = max([max(row) for row in arr])

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0 and arr[i][j] == -1:
            ans = -1
print(ans)