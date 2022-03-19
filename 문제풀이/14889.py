import sys
n = int(sys.stdin.readline())
arr = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 9999
for i in range((1 << n)):
  # print('{:04b}({})'.format(i,i))
  team1 = []
  team2 = []
  force1 = 0
  force2 = 0
  ret = 9999
  
  for j in range(n):
    # print( '{:04b}&{:04b} = {:} & {:}'.format(i,(1 << j), i , (1 << j)))
    if (i & (1 << j)):
      team2 += [j]
    
    else:
      team1 += [j]
    
    if len(team1) == (n/2 + 1) or len(team2) == (n/2 + 1):
      break

  if len(team1) == n/2 and len(team2) == n/2:
    for p in range(len(team1)):
      for q in range(p,len(team1)):
        force1 += arr[team1[p]][team1[q]]
        force1 += arr[team1[q]][team1[p]]
    for p in range(len(team2)):
      for q in range(p,len(team2)):
        force2 += arr[team2[p]][team2[q]]
        force2 += arr[team2[q]][team2[p]]
  
    ret = abs(force1 - force2)
  if answer > ret:
    answer = ret
print(answer)