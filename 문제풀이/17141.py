# import sys
# from collections import deque
# di = [0,0,1,-1]
# dj = [1,-1,0,0]

# n, m = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
# virus = []
# ans = -1
# for i in range(n):
#     for j in range(n):
#         if a[i][j] == 2:
#             a[i][j] = 0
#             virus.append((i,j))



# def bfs():
#     d = [[-1] * n for _ in range(n)]
#     q = deque()
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] == 3:
#                 q.append((i,j))
#                 d[i][j] = 0
#     while q:
#         i, j = q.popleft()
#         for k in range(4):
#             ni, nj = i + di[k], j + dj[k]
#             if 0 <= ni < n and 0 <= nj < n:
#                 if d[ni][nj] == -1 and a[ni][nj] != 1:
#                     q.append((ni,nj))
#                     d[ni][nj] = d[i][j] + 1

#     cur = 0
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] != 1:
#                 if d[i][j] == -1: return
#                 if cur < d[i][j]: cur = d[i][j]
    
#     global ans
#     if ans == -1 or ans > cur:
#         ans = cur

# def solve(idx, cnt):
#     if idx == len(virus):
#         if cnt == m:
#             bfs()
        
#     else:
#         i, j = virus[idx]
#         a[i][j] = 3
#         solve(i+1, cnt+1)
#         a[i][j] = 0
#         solve(i+1,cnt)
    
# solve(0,0)
# print(ans)

from collections import deque
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
virus = []
ans = -1
for i in range(n):
  for j in range(n):
    if a[i][j] == 2:
      a[i][j] = 0
      virus.append((i, j))

def bfs():
  d = [[-1] * n for _ in range(n)]
  q = deque()
  for i in range(n):
    for j in range(n):
      if a[i][j] == 3:
        q.append((i, j))
        d[i][j] = 0
  
  while q:
    i, j = q.popleft()
    for k in range(4):
      ni, nj = i + di[k], j + dj[k]
      if 0 <= ni < n and 0 <= nj < n:
        if a[ni][nj] != 1 and d[ni][nj] == -1:
            q.append((ni, nj))
            d[ni][nj] = d[i][j] + 1
  cur = 0
  for i in range(n):
    for j in range(n):
      if a[i][j] != 1:
        if d[i][j] == -1: return
        if cur < d[i][j]: cur = d[i][j]
  
  global ans
  if ans == -1 or ans > cur: ans = cur

def solve(idx, cnt):
  if idx == len(virus):
    if cnt == m: bfs()
  else:
    i, j = virus[idx]
    a[i][j] = 3
    solve(idx + 1, cnt+1)
    a[i][j] = 0
    solve(idx + 1, cnt)

solve(0, 0)
print(ans)
