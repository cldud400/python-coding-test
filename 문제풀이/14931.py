import sys
n, m = map(int,input().split())
arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

sum2 = 0
for t in range( 1 << (n*m) ):
  # print('{:04b}({})'.format(t,t))
  ssum = 0
  # 먼저 열부터
  for i in range(n):
    cur = 0
    for j in range(m):
      k = i*m+j
      if ( t & (1 << k) ) == 0:
        cur = cur * 10 + arr[i][j]
      else:
        ssum += cur
        cur = 0
    ssum += cur
    if sum2 < ssum:
      sum2 = ssum
  # 행 계산
  for i in range(m):
    cur = 0
    for j in range(n):
      k = j*m+i
      if ( t & (1 << k) ):
        cur = cur * 10 + arr[j][i]
      else:
        ssum += cur
        cur = 0
    ssum += cur
    if sum2 < ssum:
      sum2 = ssum
print(sum2)
