from collections import deque
import sys

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def bfs(a,i,j,size):
    ans = []
    d = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((i,j))
    d[i][j] = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and d[ni][nj] == -1:
                ok = False
                eat = False
                # 아기 상어 보다 큰 물고기가 있는칸은 지나갈 수 없다
                # 0인 칸은 지나갈 수있다
                if a[ni][nj] == 0:
                    ok = True
                # 아기상어 보다 크기가 작은 물고기는 먹을 수 있고 지나갈 수 있다.
                elif a[ni][nj] < size:
                    ok = eat = True
                # 크기가 같으면 지나갈 수 있다.
                elif a[ni][nj] == size:
                    ok = True
                # 지나갈 수 있으면
                if ok:
                    q.append((ni,nj))
                    d[ni][nj] = d[i][j] + 1
                    # 먹을 수 있으면
                    if eat:
                        ans.append((d[ni][nj], ni, nj))
    if not ans:
        return None
    ans.sort()
    return ans[0]


                


n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
i, j = 0, 0

# 아기상어 위치 찾기
for x in range(n):
    for y in range(n):
        if a[x][y] == 9:
            i, j = x, y; a[x][y] = 0

ans = 0
size = 2
exp = 0
while True:
    p = bfs(a,i,j,size)
    if p is None:
        break

    dist, ni, nj = p
    a[ni][nj] = 0
    ans += dist
    exp += 1
    if size == exp:
        size += 1
        exp = 0
    i, j = ni, nj
print(ans)

