import sys
from collections import deque, defaultdict

input = sys.stdin.readline
n = int(input())
a = defaultdict(list)

work = [0] * (n+1)
in_degree = [0] * (n+1)
d = [0] * (n+1)

for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    work[i] = tmp[0]
    for j in tmp[2:]:
        a[j].append(i)
        in_degree[i] += 1

q = deque()

for i in range(1,n+1):
    if in_degree[i] == 0:
        q.append(i)
        d[i] = work[i]


while q:
    x = q.popleft()
    for i in a[x]:
        in_degree[i] -= 1
        if d[i] < d[x] + work[i]:
            d[i] = d[x] + work[i]
        if in_degree[i] == 0:
            q.append(i)

print(max(d))
