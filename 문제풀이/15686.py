# from itertools import combinations

# n, m = map(int,input().split())
# a = [list(map(int,input().split())) for _ in range(n)]
# chicken = []
# home = []

# for i in range(n):
#   for j in range(n):
#     if a[i][j] == 2:
#       chicken.append((i,j))
#     if a[i][j] == 1:
#       home.append((i,j))

# select_chicken = list(combinations(chicken,m))


# ans = []
# for combi in select_chicken:
#     distance = 0
#     for x in home:
#         lst = []
#         for y in combi:
#             lst.append(abs(x[0]-y[0])+abs(x[1]-y[1]))
#         distance += sorted(lst)[0]
#     ans.append(distance)

# print(min(ans))


def next_permutations(a):
    
  size = len(a) - 1
  i = size
  # while i <= size and a[i-1] < a[i]:
  #   i += 1
  # i -= 1
  while i > 0 and a[i-1] >= a[i]:
    i -= 1

  if i <= 0: return False
  
  j = size
  while a[j] <= a[i-1]:
    j -= 1

  a[i-1], a[j] = a[j], a[i-1]

  j = size
  while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1
  
  return True

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

house = []
store = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1: house.append((i,j))
        elif a[i][j] == 2: store.append((i,j))

d = [0] * len(store)

for i in range(m):
    d[i] = 1

d.sort()
ans = -1
while True:
    s = 0
    for i, j in house:
        dist = []
        for k, (si,sj) in enumerate(store):
            if d[k] == 0: continue
            d1 = abs(i-si)
            d2 = abs(j-sj)
            dist.append(d1+d2)
        dist.sort()
        s += dist[0]
    if ans == -1 or ans > s: ans = s
    if not next_permutations(d): break
print(ans)