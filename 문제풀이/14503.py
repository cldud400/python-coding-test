n , m = map(int,input().split())
r, c, d= map(int,input().split())


# arr = [[1,1,1],[1,0,1],[1,1,1]]
arr = []
for i in range(n):
  lst = list(map(int, input().split()))
  arr.append(lst)

cnt = 0

di = [-1,0,1,0]
dj = [0,1,0,-1]

while True:
  if arr[r][c] == 0:
    arr[r][c] = 2
  
  if arr[r+1][c] != 0 and arr[r-1][c] != 0 and arr[r][c-1] != 0 and arr[r][c+1] != 0:
    if arr[r-di[d]][c-dj[d]] == 1:
      break
    else:
      r -= di[d]
      c -= dj[d]
  else:
    d = (d + 3) % 4
    if arr[r+di[d]][c+dj[d]] == 0:
      r += di[d]
      c += dj[d]


for i in range(n):
  for j in range(m):
    if arr[i][j] == 2:
      cnt += 1

print(cnt)