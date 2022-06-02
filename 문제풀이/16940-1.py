import sys
from collections import deque

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().split())
    i, j = i-1, j-1
    a[i].append(j)
    a[j].append(i)

order = list(map(int, input().split()))
order = [x-1 for x in order]
check = [False] * n
parent = [-1] * n

q = deque()
q.append(0)
check[0] = True
m = 1

for i in range(n):
    if not q: print(0); exit(0)

    x = q.popleft()
    if x != order[i]: print(0); exit(0)

    cnt = 0
    for j in a[x]:
        if check[j] == False:
            parent[j] = x
            cnt += 1

    for k in range(cnt):
        if m+k >= n or parent[order[m+k]] != x:
            print(0)
            exit(0)
        q.append(order[m+k])
        check[order[m+k]] = True
    m += cnt
print(1)