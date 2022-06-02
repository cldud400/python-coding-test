n, m, r = map(int,input().split())
arr = [list(map(int, list(input().split()))) for _ in range(n)]

groups = []
groupk = min(n,m) // 2

for k in range(groupk):
  group = []
  for j in range(k, m-k):
    group.append(arr[k][j])
  for i in range(k+1,n-k-1):
    group.append(arr[i][m-k-1])
  for j in range(m-k-1,k,-1):
    group.append(arr[n-k-1][j])
  for i in range(n-k-1,k,-1):
    group.append(arr[i][k])

  groups.append(group)



for k in range(groupk):
  group = groups[k]
  size = len(group)
  idx = r%size
  for j in range(k, m-k):
    arr[k][j] = group[idx]
    idx = (idx + 1) % size
  for i in range(k+1,n-k-1):
    arr[i][m-k-1] = group[idx]
    idx = (idx + 1) % size
  for j in range(m-k-1,k,-1):
    arr[n-k-1][j] = group[idx]
    idx = (idx + 1) % size
  for i in range(n-k-1,k,-1):
    arr[i][k] = group[idx]
    idx = (idx + 1) % size

for line in arr:
  print(*line)

