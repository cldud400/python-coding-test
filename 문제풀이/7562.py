import sys
from collections import deque
from collections import defaultdict
# sys.setrecursionlimit(100000)
t = int(sys.stdin.readline())

di = [-1, -2, -2, -1, 1, 2, 2, 1]
dj = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs():
        while queue:
            i,j = queue.popleft()
            check[i][j] = 1
            for k in range(8):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < l and 0 <= nj < l:
                    if arr[ni][nj] == 0 and check[ni][nj] == 0: # 방문한 적이 없고 길이 있을 때
                        queue.append((ni,nj))
                        arr[ni][nj] = arr[i][j] + 1
                        check[ni][nj] = 1
                if arr[dx][dy] != 0:
                    break

                    

                        
for _ in range(t):
    l = int(sys.stdin.readline())
    x, y = map(int,sys.stdin.readline().split())
    dx, dy = map(int,sys.stdin.readline().split())

    check = [[0] * l for _ in range(l)]
    arr = [[0]* l for _ in range(l)]
    arr[dx][dy] == -1
    queue = deque()
    queue.append((x,y))


    bfs()
        
    print(arr[dx][dy])
    print(arr)
    

