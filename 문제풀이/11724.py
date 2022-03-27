import sys
from collections import deque
from collections import defaultdict
# sys.setrecursionlimit(100000)
n, m= map(int,sys.stdin.readline().split())

# 인접 행렬을 이용한 BFS
arr = [[0] * (n+1) for _ in range(n+1)]

# 인접 리스트를 이용한 BFS
al = defaultdict(list)



for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    # 인접 행렬
    arr[i][j] = arr[j][i] = 1

    # 인접 리스트
    al[i].append(j)
    al[j].append(i)

check = [0] * (n+1)
# 인접 리스트(DFS)
def dfs(x):
    check[x] = 1
    for i in al[x]:
        if check[i] == 0:
            dfs(i)


cnt = 0
for i in range(1, n+1):
    if not check[i]:
        dfs(i)
        cnt += 1

print(cnt)
