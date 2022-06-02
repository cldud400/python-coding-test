import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
next = list(range(101))
dist = [-1] * 101

for _ in range(n+m):
    x, y = map(int, sys.stdin.readline().split())
    next[x] = y

dist[1] = 0
q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in range(1, 7):
        j = x + i
        if j > 100: continue
        j = next[j]
        if dist[j] == -1:
            dist[j] = dist[x] + 1
            q.append(j)
print(dist[100])