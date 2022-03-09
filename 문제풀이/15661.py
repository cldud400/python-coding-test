def solve(i=0, team1=[], team2=[]):
    if i ==n:
        if len(team1) ==0 or len(team2) == 0: return -1

    # 각 팀의 능력치를 구해서 차이를 돌려준다
    force1 = 0
    force2 = 0
    for i in team1:
        for j in team1:
            if i == j: continue
            force1 += arr[i][j]

    for i in team2:
        for j in team2:
            if i == j: continue
            force2 += arr[i][j]

    return abs(force1 - force2)

    answer = -1

    ret = solve(i+1, team1 + [i], team2)
    if answer == -1 or (ret != -1 and answer > ret):
        answer = ret

    ret = solve(i+1, team1, team2 + [i])
    if answer == -1 or (ret != -1 and answer > ret): 
        answer = ret
    return answer

import sys
n = int(sys.stdin.readline())
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

print(solve())