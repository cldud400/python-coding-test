from copy import deepcopy
n, m, d = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

# 시뮬레이션
def solve(i1,i2,i3):
    b = deepcopy(a)
    ans = 0
    while True:
        cnt = 0
        # 적의 수를 확인
        for i in range(n):
            for j in range(m):
                cnt += b[i][j]

        if cnt == 0: break

        # 한번에 처리할 수 있는 적의 수는 최대 3
        deleted = [(-1,-1)] * 3
        archer = [i1,i2,i3]

        # 궁수의 순서대로 처리
        for k in range(3):
            ni, nj = n, archer[k]
            xi, xj, dist = -1, -1, -1
            for j in range(m):
                for i in range(n):
                    if b[i][j] != 0:
                        di = abs(ni-i)
                        dj = abs(nj-j)
                        dd = di + dj
                        # 적이 궁수의 사정거리 내에 있어야 한다
                        # 제일 가까운 적 처리
                        if dd <= d:
                            if dist == -1 or dist > dd:
                                xi = i
                                xj = j
                                dist = dd
            # 처리 된 적 
            deleted[k] = (xi,xj)

        # 처리된 적의 수 확인
        for i,j in deleted:
            if i == -1: continue
            if b[i][j] != 0: 
                ans += 1
                b[i][j] = 0
        
        # 처리가 끝나면 적이 이동한다.
        for i in range(n-1,-1,-1):
            for j in range(m):
                if i == 0: b[i][j] = 0
                else: b[i][j] = b[i-1][j]

    return ans





# 가능한 궁수 배치는 m^3 for 3개로 처리
ans = 0
for i1 in range(m):
    for i2 in range(i1+1,m):
        for i3 in range(i2+1,m):
            ret = solve(i1,i2,i3)
            if ans < ret: ans = ret

print(ans)


