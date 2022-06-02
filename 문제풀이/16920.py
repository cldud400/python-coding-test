from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

n, m, p = map(int,input().split())
s = [0] + list(map(int,input().split()))
a = [[0] * m for _ in range(n)]


# .(빈곳)= 0, #(벽) = -1
for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == '.': a[i][j] = 0
        elif line[j] == '#': a[i][j] = -1
        else: a[i][j] = int(line[j])

q = [ deque() for _ in range(p+1)]
nq = [ deque() for _ in range(p+1)]

for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            q[a[i][j]].append((i,j))

while True:
    flag = False
    for player in range(1, p+1):
        d = [[0] * m for _ in range(n)]
        while q[player]:
            flag = True
            i, j = q[player].popleft()
            if d[i][j] == s[player]: nq[player].append((i,j))
            if a[i][j] > 0 and a[i][j] != player: continue
            a[i][j] = player
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if a[ni][nj] == 0:
                        d[ni][nj] = d[i][j] + 1
                        if d[ni][nj] <= s[player]:
                            a[ni][nj] = player
                            q[player].append((ni,nj))

        q[player] = nq[player]
        nq[player] = deque()
    if not flag: break

ans = [0] * (p+1)
for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            ans[a[i][j]] += 1
print(*ans[1:])
