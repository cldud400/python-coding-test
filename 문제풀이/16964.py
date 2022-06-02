import sys
from collections import deque

n = int(input())
a = [[] for _ in range(n+1)]
for _ in range(n-1):
    i, j = map(int, sys.stdin.readline().split())
    i, j = i-1, j-1
    a[i].append(j)
    a[j].append(i)

b = list(map(int, input().split()))
b = [x-1 for x in b]
order = [0] * n
check = [False] * (n)

for i in range(n):
    order[b[i]] = i

for i in range(n):
    a[i].sort(key=lambda x: order[x])

dfs_order = []
check = [False] * n

def dfs(x):
    if check[x]: return
    dfs_order.append(x)
    check[x] = True
    for j in a[x]:
        dfs(j)
dfs(0)

flag = True

for i in range(n):
    if dfs_order[i] != b[i]: flag = False
if flag:
    print(1)
else:
    print(0)




