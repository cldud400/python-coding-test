import sys
sys.setrecursionlimit(1000000)

n = int(input())
a = [list(input().rstrip()) for _ in range(n)]
color = [[-1]*n for _ in range(n)]

di = [-1,-1,0,0,1,1]
dj = [0,1,-1,1,-1,0]

ans = 0



def dfs(i,j,c):
    global ans
    color[i][j] = c
    ans = max(ans, 1)
    for k in range(6):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            if a[ni][nj] == 'X':
                if color[ni][nj] == -1: dfs(ni,nj,1-c)
                ans = max(ans, 2)
                if color[ni][nj] == c: ans = max(ans, 3)

for i in range(n):
    for j in range(n):
        if a[i][j] == 'X' and color[i][j] == -1:
            dfs(i,j,0)


print(ans)





