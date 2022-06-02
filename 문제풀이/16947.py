import sys
from collections import deque

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n):
    i, j = map(int,(input().split()))
    i -= 1
    j -= 1
    a[i].append(j)
    a[j].append(i)


check = [0] * n # 0: 방문X, 1: 방문O, 2: 싸이클

#싸이클을 찾는다
def solve(x, p):
    # -2: 싸이클을 찾은 경우(포함되지 않은 경우)
    # -1: 싸이클을 찾지 못한 경우
    # 0 ~ n-1: 싸이클을 찾은 경우 (포함되는 경우)
    if check[x] == 1: return x

    check[x] = 1
    for i in a[x]:
        if i == p: continue
        result = solve(i, x)
        if result == -2: return -2
        if result >= 0:
            check[x] = 2
            if x == result: return -2
            else: return result
    return -1

solve(0,-1)

q = deque()
dist = [-1]*n
for i in range(n):
    if check[i] == 2:
        dist[i] = 0
        # 싸이클에 포함된 노드를 시작 노드로 지정
        q.append(i)
    else:
        dist[i] = -1


# 싸이클에 포함되지 않는 노드에서 포함되는 노드로 최단거리
while q:
    x = q.popleft()
    for i in a[x]:
        if dist[i] == -1:
            q.append(i)
            dist[i] = dist[x] + 1

print(*dist)

