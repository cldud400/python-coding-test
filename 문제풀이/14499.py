# n, m, i, j, r = 4, 2, 0, 0, 8
# arr = [[0,2],[3,4],[5,6],[7,8]]
n, m, i, j, r = map(int,input().split())
arr = [list(map(int, list(input().split()))) for _ in range(n)]
dice = [0] * 7

di = [0,0,-1,1]
dj = [1,-1,0,0]

move = list(map(int, list(input().split())))
for k in move:
  ni, nj = i + di[k-1], j + dj[k-1]

  if ni < 0 or ni >= n or nj < 0 or nj >= m:
    continue

  if k == 1:
    dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]

  elif k == 2:
    dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]

  elif k == 3:
    dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
  
  else:
    dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]


  i = ni
  j = nj

  if arr[i][j] == 0:
    arr[i][j] = dice[6]
  else:
    dice[6] = arr[i][j]
    arr[i][j] = 0

  print(dice[1])
