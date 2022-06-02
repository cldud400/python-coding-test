import sys
from collections import deque

di = [0, 0, 1, -1,1,-1,1,-1,0]
dj = [1, -1, 0, 0,1,-1,-1,1,0]
n = 8
a = [list(list(input())) for _ in range(n)]

check = [[[False] * (n+1) for _ in range(n)] for _ in range(n)]

q = deque()
q.append((7,0,0))
check[7][0][0] = True
ans = False



while q:
    i, j, t = q.popleft()
    if i == 0 and j == 7:
        ans = True
    for k in range(9):
        ni, nj = i + di[k], j + dj[k]
        nt = min(t+1, 8)
        if 0 <= ni < n and 0 <= nj < n:
            if ni - t >= 0 and a[ni-t][nj] == '#': continue
            if ni-t-1 >= 0 and a[ni-t-1][nj] == '#': continue
            if check[ni][nj][nt] == False:
                check[ni][nj][nt] = True
                q.append((ni,nj,nt))


if ans: print(1)
else: print(0)
