from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]
n, m = map(int,input().split())

a = [list(input()) for _ in range(n)]
d = [[[[-1]*4 for _ in range(4)]for _ in range(m)] for _ in range(n)]

q = deque()

x1,y1,x2,y2 = -1,-1,-1,-1
ans = -1

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            for k in range(4):
                q.append((i,j,k,0))
                d[i][j][k][0] = 0
        elif a[i][j] == 'C':
            if x1 == -1: x1, y1 = i, j
            else: x2, y2 = i, j


while q:
    i, j, dir, s = q.popleft()
    
    if s == 3: ans = d[i][j][dir][s]; break

    for k in range(4):
        if dir == k: continue
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            if a[ni][nj] != '#':
                ns = s
                if a[ni][nj] == 'C':
                    if ni == x1 and nj == y1: ns |= 1
                    else: ns |= 2

                if d[ni][nj][k][ns] == -1:
                    d[ni][nj][k][ns] = d[i][j][dir][s] + 1
                    q.append((ni,nj,k,ns))

print(ans)


