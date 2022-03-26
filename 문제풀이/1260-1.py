import sys
from collections import deque
from collections import defaultdict
n, m, v = map(int,sys.stdin.readline().split())

# 인접 행렬을 이용한 BFS
arr = [[0] * (n+1) for _ in range(n+1)]

# 인접 리스트를 이용한 BFS
al = defaultdict(list)

check = [False] * (n+1)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    # 인접 행렬
    arr[i][j] = arr[j][i] = 1

    # 인접 리스트
    al[i].append(j)
    al[j].append(i)

#인접 리스트을 정렬 해준다.
for i in range(n):
    al[i].sort()


# 인접 행렬
def bfs(start):
    queue = deque()
    queue.append(start)
    check[start] = True
    while queue:
        x = queue.popleft()
        print(x, end = ' ')
        for i in range(1, n+1):
            if arr[x][i] == 1 and check[i] == False:
                check[i] = True
                queue.append(i)

# # 인접 리스트
# def bfs(start):
#     queue = deque()
#     queue.append(start)
#     check[start] = True
#     while queue:
#         x = queue.popleft()
#         print(x, end = ' ')
#         for i in al[x]:
#             if check[i] == False:
#                 check[i] = True
#                 queue.append(i)



bfs(v)