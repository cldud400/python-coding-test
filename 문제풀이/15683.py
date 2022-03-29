di = [0,1,0,-1]
dj = [1,0,-1,0]
def check(a, b, x, y, dir):
    i, j = x, y
    while 0 <= i < n and 0 <= j < m:
        if a[i][j] == 6: break
        b[i][j] = a[x][y]
        i += di[dir]
        j += dj[dir]


def solve(a, cctv, idx, dirs):
    if len(cctv) == idx:
        b = [row[:] for row in a]
        for k , (w, i, j) in enumerate(cctv):
            if w == 1:
                check(a,b,i,j,dirs[k])
            elif w == 2:
                check(a,b,i,j,dirs[k])
                check(a,b,i,j,(dirs[k] + 2) % 4)
            elif w == 3:
                check(a,b,i,j,dirs[k])
                check(a,b,i,j,(dirs[k] + 1) % 4)
            elif w == 4:
                check(a,b,i,j,dirs[k])
                check(a,b,i,j,(dirs[k] + 1) % 4)
                check(a,b,i,j,(dirs[k] + 2) % 4)
            elif w == 5:
                check(a,b,i,j,dirs[k])
                check(a,b,i,j,(dirs[k] + 1) % 4)
                check(a,b,i,j,(dirs[k] + 2) % 4)
                check(a,b,i,j,(dirs[k] + 3) % 4)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if b[i][j] == 0:
                    cnt += 1
        return cnt
    ans = 100
    for i in range(4):
        ret = solve(a,cctv,idx+1,dirs+[i])
        if ans > ret: ans = ret
    return ans



n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

# cctv 위치 확인
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= a[i][j] <= 5:
            cctv.append((a[i][j], i, j))

print(solve(a, cctv, 0, []))