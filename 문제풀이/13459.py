

di = [0,0,1,-1]
dj = [1,-1,0,0]

class Marble:
  def __init__(self, moved, hole, i, j):
    self.moved = moved
    self.hole = hole
    self.i = i
    self.j = j

def simulate(a, k, i, j):
  n = len(a)
  m = len(a[0])

  if a[i][j] == '.': return Marble(False,False,i,j)
  moved = False
  while True:
    ni,nj = i+ di[k], j + dj[k]
    if ni < 0 or ni >= n or nj < 0 or nj >= m:
      return Marble(moved, False, i, j)

    ch = a[ni][nj]
    if ch == '#': return Marble(moved, False, i, j) 
    elif ch in 'RB': return Marble(moved, False, i, j) 
    elif ch  == '.':
        a[i][j], a[ni][nj] = a[ni][nj], a[i][j]
        i, j = ni, nj
        moved = True
    elif ch == 'O':
        a[i][j] = '.'
        moved = True
        return Marble(moved, True, i, j) 



def check(a, dirs):
  n = len(a)
  m = len(a[0])
  hi, hj = 0,0
  ri, rj = 0,0
  bi, bj = 0,0


  # 구멍, 빨간구슬, 파란구슬의 위치를 확인
  for i in range(n):
    for j in range(m):
      if a[i][j] == 'O': hi,hj = i, j
      if a[i][j] == 'R': ri,rj = i, j
      if a[i][j] == 'B': bi,bj = i, j

  cnt = 0
  # 방향에 따라서, 구슬을 굴려보면서 몇번만에 들어가는지 시뮬레이션 한다.
  for k in dirs:
    cnt += 1
    hole1 = hole2 = False
    while True:
      p1 = simulate(a, k, ri, rj)
      ri, rj = p1.i, p1.j
      p2 = simulate(a, k, bi, bj)
      bi, bj = p2.i, p2.j

      if not p1.moved and not p2.moved: break
      if p1.hole: hole1 = True
      if p2.hole: hole2 = True

    if hole2: return -1
    if hole1: return cnt
  return -1
    


def valid(dirs):
  # 왼쪽 오른쪽 위 아래를 왔다갔다 하는건 의미가 없다.
  # 같은 방향으로 가는 것도 의미 없다.
  l = len(dirs)
  for i in range(l-1):
    if dirs[i] == 0 and dirs[i+1] == 1: return False
    if dirs[i] == 1 and dirs[i+1] == 0: return False
    if dirs[i] == 2 and dirs[i+1] == 3: return False
    if dirs[i] == 3 and dirs[i+1] == 2: return False
    if dirs[i] == dirs[i+1]: return False
  return True

n, m = map(int,input().split())
board = [input() for _ in range(n)]
ans = -1

for k in range( 1<< (10*2)):
  # 경우의 수
  dirs = [0] * 10
  for i in range(10): dirs[i] = (k & 3); k >>= 2
  if not valid(dirs): continue

  a = [list(row) for row in board]
  ret = check(a, dirs)
  if ret == -1: continue
  if ans == -1 or ans > ret: ans = ret


if ans == -1:
    ans = 0
else:
    ans = 1
print(ans)


