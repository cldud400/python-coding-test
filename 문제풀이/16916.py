#DFS를 사용
di = [0,0,1,-1]
dj = [1,-1,0,0]
n, m = map(int,input().split())
a = [input() for _ in range(n)]
dist = dist = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]

def solve(i,j,cnt,color):
  if check[i][j]:
    if cnt - dist[i][j]  >= 4: return True
    else: return False

  check[i][j] = True
  dist[i][j] = cnt
  for k in range(4):
    ni, nj = i + di[k], j + dj[k]
    if 0 <= ni < n and 0 <= nj < m:
      if a[ni][nj] == color:
        if solve(ni,nj,cnt+1,color): return True
  return False

for i in range(n):
  for j in range(m):
    if check[i][j]: continue
    dist = dist = [[0]*m for _ in range(n)]
    ok = solve(i,j,1,a[i][j])
    if ok: print('Yes'); exit()

print('No')