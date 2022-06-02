import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10000000)

input = sys.stdin.readline
n, m = map(int,input().split())

a = defaultdict(list)

in_degree = [0] * (n+1)
for _ in range(m):
    i, j = map(int,input().split())
    # i -> j
    a[i].append(j)
    # j번째에 들어오는 간선의 수
    in_degree[j] += 1

q = deque()

# in_degree가 0인 노드가 시작노드
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)
# BFS
while q:
    x = q.popleft()
    print(x, end = ' ')
    for i in a[x]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)
print()

# check = [False] * (n+1)
# for _ in range(m):
#     i, j = map(int,input().split())
#     # i -> j
#     a[j].append(i)


# q = deque()


# # DFS
# def solve(x):
#     check[x] = True
#     for i in a[x]:
#         if check[i] == False:
#             solve(i)
#     print(x, end = ' ')

# for i in range(1, n+1):
#     if check[i] == False:
#         solve(i)
# print()