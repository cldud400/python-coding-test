# from collections import deque
# from collections import defaultdict

# n, m, r = map(int,input().split())
# arr = [list(map(int, list(input().split()))) for _ in range(n)]
# P = min(n,m)//2

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# cycle = (n-1) * 2 + (m-1) * 2

# def solve(i,r):
#   for _ in range(r):
#     x, y = i, i
#     corner = [[n-1,i],[n-1,m-1],[i,m-1],[i,i]]
#     value = arr[x][y]
#     k = 0
#     while True:
#       if k == 4:
#         break
#       nx, ny = x + dx[k], y + dy[k]
#       next = arr[nx][ny]
#       arr[nx][ny] = value
#       x, y = nx, ny
#       value = next
#       if nx == corner[k][0] and ny == corner[k][1]:
#         k += 1


# for i in range(P):
#     solve(i,r%cycle)
#     n -= 1
#     m -= 1
#     cycle -= 8

# for line in arr:
#     print(*line)

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