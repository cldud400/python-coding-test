import sys
from collections import deque
# sys.setrecursionlimit(1000000)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m= map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

arr = [[0]* m for _ in range(n)]
queue = deque()

arr[0][0] = 1 # 0,0에서 출발
queue.append((0,0))
def bfs():
    while queue:
        i,j = queue.popleft() 
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 0 and maze[ni][nj] == 1: # 방문한 적이 없고 길이 있을 때
                    queue.append((ni,nj))
                    arr[ni][nj] = arr[i][j] + 1 # 이전 경로 +1

bfs()
print(arr[n-1][m-1])
