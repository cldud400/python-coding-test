from collections import deque
n, k = map(int,input().split())

a = [input() for _ in range(2)]
dir = [(0,1),(0,-1),(1,k)]
d = [[-1] * n for _ in range(2)]

q = deque()
q.append((0,0))
d[0][0] = 0
flag = False

while q:
    i, j = q.popleft()
    for di, dj in dir:
        ni, nj = (i + di)%2, j + dj
        if nj >= n: flag = True; break

        if nj < 0: continue
        if d[ni][nj] != -1: continue
        if a[ni][nj] == '0': continue
        if nj < d[i][j] + 1: continue
        d[ni][nj] = d[i][j] + 1
        q.append((ni,nj))
        
    if flag: break

if flag:
    print(1)
else:
    print(0)
    


