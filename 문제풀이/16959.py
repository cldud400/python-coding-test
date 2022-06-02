from collections import deque

# 나이트
di1 = [-1, 1, 2, 2, 1, -1, -2, -2]
dj1 = [2, 2, 1, -1, -2, -2, -1, 1]
# 룩
di2 = [0,0,1,-1]
dj2 = [1,-1,0,0]
# 비숍
di3 = [-1, 1, 1, -1]
dj3 = [1, 1, -1, -1]



n = int(input())
a = [list(map(int,(input().split()))) for _ in range(n)]
d = [[[[-1] * 3 for _ in range(n*n)] for _ in range(n)] for _ in range(n)]


q = deque()
for i in range(n):
    for j in range(n):
        a[i][j] -= 1
        if a[i][j] == 0:
            for k in range(3):
                d[i][j][0][k] = 0
                q.append((i,j,0,k))


ans = -1
while q:
    i,j,num,piece = q.popleft()
    if num == n*n -1:
        if ans == -1 or ans > d[i][j][num][piece]:
            ans = d[i][j][num][piece]
    
    for k in range(3):
        if piece == k: continue
        if d[i][j][num][k] == -1:
            d[i][j][num][k] = d[i][j][num][piece] + 1
            q.append((i,j,num,k))
    
    # 나이트
    if piece == 0:
        for k in range(8):
            ni,nj = i + di1[k], j + dj1[k]
            if 0 <= ni < n and 0 <= nj < n:
                nextN = num
                if a[ni][nj] == num + 1: nextN = num + 1
                if d[ni][nj][nextN][piece] == -1:
                    d[ni][nj][nextN][piece] = d[i][j][num][piece] + 1
                    q.append((ni,nj,nextN,piece))
    # 룩
    elif piece == 1:
        for k in range(4):
            L = 1
            while True:
                ni,nj = i + di2[k] * L, j + dj2[k] * L
                if 0 <= ni < n and 0 <= nj < n:
                    nextN = num
                    if a[ni][nj] == num + 1: nextN = num + 1
                    if d[ni][nj][nextN][piece] == -1:
                        d[ni][nj][nextN][piece] = d[i][j][num][piece] + 1
                        q.append((ni,nj,nextN,piece))
                else: break
                L += 1
    # 비숍
    else:
        for k in range(4):
            L = 1
            while True:
                ni,nj = i + di3[k] * L, j + dj3[k] * L
                if 0 <= ni < n and 0 <= nj < n:
                    nextN = num
                    if a[ni][nj] == num + 1: nextN = num + 1
                    if d[ni][nj][nextN][piece] == -1:
                        d[ni][nj][nextN][piece] = d[i][j][num][piece] + 1
                        q.append((ni,nj,nextN,piece))
                else: break
                L += 1

print(ans)



