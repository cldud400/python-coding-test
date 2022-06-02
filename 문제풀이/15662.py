
n = int(input())
gear = [list(map(int,input())) for _ in range(n)]
k = int(input())


for _ in range(k):
  no, dir = map(int,input().split())
  no -= 1
  d = [0] * n 
  d[no] = dir # 회전하는 톱니바퀴 찾기

  # 회전 해야하는 톱니바퀴의 방향을 결정
  for i in range(no-1, -1, -1):
    if gear[i][2] != gear[i+1][6]:
      d[i] = - d[i+1]
    else:
      break

  for i in range(no+1, n):
    if gear[i-1][2] != gear[i][6]:
      d[i] = -d[i-1]

    else:
      break

  # 4개의 톱니바퀴를 회전
  for i in range(n):
    if d[i] == 0:
      continue

    if d[i] == 1:
      tmp = gear[i][7]
      for j in range(7,0,-1):
        gear[i][j] = gear[i][j-1]
      gear[i][0] = tmp

    elif d[i] == -1:
      tmp = gear[i][0]
      for j in range(0,7):
        gear[i][j] = gear[i][j+1]
      gear[i][7] = tmp



ans = 0

for i in gear:
    if i[0] == 1:
        ans += 1

print(ans)