from collections import deque
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

def bfs():
    ans = 0
    check = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2 and check[i][j] == False:
                dead = True
                q = deque()
                q.append((i,j))
                check[i][j] = True
                cur = 0
                while q:
                    cur += 1
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + di[k], y + dj[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if a[nx][ny] == 0: dead = False
                            elif a[nx][ny] == 2 and check[nx][ny] == False:
                                q.append((nx,ny))
                                check[nx][ny] = True
                if dead: ans += cur
    return ans
                            

ans = 0

# 모든 위치에 돌을 놓는다
for i1 in range(n):
    for j1 in range(m):
        if a[i1][j1] !=0: continue # 빈공간이 아니면 돌을 놓을 수 없다
        for i2 in range(n):
            for j2 in range(m):
                if a[i2][j2] != 0: continue
                if i1 == i2 and j1 == j2: continue

                a[i1][j1] = 1
                a[i2][j2] = 1
                result = bfs()
                if ans < result: ans = result
                a[i1][j1] = 0
                a[i2][j2] = 0

print(ans)