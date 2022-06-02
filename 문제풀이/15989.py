n = 10000
d = [0] * (n+1)
d[0] = 1
for i in range(1, n+1):
  if i-1 >= 0:
    d[i] += d[i-1]
for i in range(1, n+1):
  if i-2 >= 0:
    d[i] += d[i-2]
for i in range(1, n+1):
  if i-3 >= 0:
    d[i] += d[i-3]


# t = int(input())
# d = [[0]*3 for _ in range(10001)]
# d[1] = [1,0,0]
# d[2] = [1,1,0]
# d[3] = [1,1,1]
# for i in range(4,10001):
#   d[i][0] = 1
#   d[i][1] = 1 + d[i-2][1]
#   d[i][2] = d[i-3][0] + d[i-3][1] + d[i-3][2]
# for _ in range(t):
#   n = int(input())
#   print(sum(d[n]))