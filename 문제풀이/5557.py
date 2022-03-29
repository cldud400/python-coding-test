n = int(input())
a = list(map(int,input().split()))

d = [[0] * (21) for _ in range(n)]
d[0][a[0]] = 1

for i in range(1,n-1):
  for j in range(21):
    if d[i-1][j]:
      if 0 <= j+a[i] <= 20: d[i][j+a[i]] += d[i-1][j]
      if 0 <= j-a[i] <= 20: d[i][j-a[i]] += d[i-1][j]
  
print(d[n-2][a[-1]])