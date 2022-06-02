import sys
from collections import deque

n = int(input())

dr = [-2,-2,0,0,2,2]
dc = [-1,1,-2,2,-1,1]

a = [[-1] * n for _ in range(n)]

r1, c1, r2, c2 = map(int, input().split())

q = deque()
q.append((r1,c1))
a[r1][c1] = 0

while q:
    r,c = q.popleft()
    for k in range(6):
        x, y = r + dr[k], c + dc[k]
        if 0 <= x < n and 0 <= y < n:
            if a[x][y] == -1:
                q.append((x,y))
                a[x][y] = a[r][c] + 1

print(a[r2][c2])