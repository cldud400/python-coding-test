import sys
from collections import deque
from collections import defaultdict
n, m, v = map(int,sys.stdin.readline().split())

# 인접 행렬을 이용한 DFS
arr = [[0] * (n+1) for _ in range(n+1)]

# 인접 리스트를 이용한 DFS
al = defaultdict(list)


check = [False] * (n+1)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    # 인접 행렬
    arr[i][j] = arr[j][i] = 1

    # 인접 리스트
    al[i].append(j)
    al[j].append(i)

# 인접 행렬을 정렬 해준다.
# for i in range(n):
#     al[i].sort()

# # 재귀를 사용
# # 인접 행렬
# def dfs(x):
#     check[x] = True
#     print(x, end = ' ')
#     for i in range(1, n+1):
#         if arr[x][i] == 1 and check[i] == False:
#             dfs(i)

# # 인접 리스트
# def dfs(x):
#     check[x] = True
#     print(x, end = ' ')
#     for i in al[x]:
#         if check[i] == False:
#             dfs(i)

# stack를 사용
# 인접 행렬
def dfs(start):
    check = [False] * (n+1)
    stack = deque()

    stack.append(start)
    check[start] = True
    while stack:
        x = stack.pop()
        print(x, end = ' ')
        for i in range(n, -2, -1):
            if arr[x][i] == 1 and check[i] == False:
                check[i] = True
                stack.append(i)


# # 인접 리스트
# def dfs(start):
#     check = [False] * (n+1)
#     stack = deque()

#     stack.append(start)
#     check[start] = True
#     while stack:
#         x = stack.pop()
#         print(x, end = ' ')
#         for i in al[x]:
#             if check[i] == False:
#                 check[i] = True
#                 stack.append(i)

dfs(v)


