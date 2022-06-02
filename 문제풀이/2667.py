import sys
from collections import deque
# sys.setrecursionlimit(100000)

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n = int(sys.stdin.readline())

apt = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

# 인접행렬
arr = [[0] * n for _ in range(n)]

def dfs(i, j, num): # num = 단지번호
    arr[i][j] = num
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            if apt[ni][nj] == 1 and arr[ni][nj] == 0:   # 옆에 건물이 있는데 인접행렬이 0 이면
                dfs(ni,nj,num) # 인접 행렬을 1로 바꾸고 좌표를 옮긴다


num = 0
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1 and arr[i][j] == 0:
            num += 1
            dfs(i,j,num)        # 단지 하나를 순회하고 num += 1
            


cnt = [0] * (num+1)
for i in range(n):
    for j in range(n):
        for k in range(1, num+1):
            if arr[i][j] == k:
                cnt[k] += 1


print(num)
print(*sorted(cnt[1:]), sep = '\n')




