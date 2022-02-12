n, s, m = map(int,input().split())
a =list(map(int,input().split())) + [0]
d = [[0] * (m+1) for _ in range(n+1)]

d[0][s] = 1

for i in range(n):
  for j in range(m+1):
    if d[i][j] != 0:
      if j - a[i] > -1:
        d[i+1][j-a[i]] = d[i][j]
      if j + a[i] < m+1:
        d[i+1][j+a[i]] = d[i][j]
    if d[i] == [0] * (m+1):
      break
ans = -1
for i in range(m+1):
  if d[-1][i] != 0:
    ans = i
if ans != -1:
  print(ans)
else:
  print(-1)