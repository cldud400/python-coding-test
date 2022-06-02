arr = [[0] * 101 for _ in range(101)]
n = int(input())

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

def curve(x,y,dir,gen):
  ans = [dir]
  for _ in range(gen):
    tmp = ans[:]
    tmp = tmp[::-1]
    for i in range(len(tmp)):
      tmp[i] = (tmp[i]+1) % 4
    ans += tmp
  return ans

check = [[0] * 101 for _ in range(101)]

for _ in range(n):
  y, x, dir, gen = map(int,input().split())
  dirs = curve(x,y,dir,gen) 
  check[x][y] = 1
  for d in dirs:
    x += di[d]
    y += dj[d]
    check[x][y] = 1


cnt = 0

for i in range(100):
  for j in range(100):
    if check[i][j] and check[i+1][j] and check[i+1][j+1] and check[i][j+1]:
      cnt += 1

  

print(cnt)