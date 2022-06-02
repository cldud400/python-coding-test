from itertools import permutations

n = int(input())

a = [list(map(int,input().split())) for _ in range(n)]

ans = 0

def solve(arr):
    batter = 0
    score = 0
    for inning in a:
        out = 0
        base1,base2,base3 = 0,0,0
        while out < 3:
            if inning[arr[batter]] == 0:
                out += 1
            elif inning[arr[batter]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif inning[arr[batter]] == 2:
                score += (base2+base3)
                base1, base2, base3 = 0, 1, base1
            elif inning[arr[batter]] == 3:
                score += (base1+base2+base3)
                base1, base2, base3 = 0, 0, 1
            elif inning[arr[batter]] == 4:
                score += (1+base1+base2+base3)
                base1, base2, base3 = 0, 0, 0

            
            batter = (batter+1) % 9
    
    return score

for perm in permutations(range(1,9),8):
    perms = list(perm[:3]) + [0] + list(perm[3:])
    ans = max(ans, solve(perms))

print(ans)