def solve(z):
    if z == 81:
        for row in a:
            print(*row, sep = ' ')

        return True
    
    x = z// n
    y = z % n

    if a[x][y] != 0: return solve(z+1)
    else:
        for i in range(1,10):
            if c0[x][i] == False and c1[y][i] == False and c2[(x//3)*3+(y//3)][i] == False:
                c0[x][i] = c1[y][i] = c2[(x//3)*3+(y//3)][i] = True
                a[x][y] = i
                if solve(z+1): return True
                a[x][y] = 0
                c0[x][i] = c1[y][i] = c2[(x//3)*3+(y//3)][i] = False
    
    return False








n = 9
a = [list(map(int,input().split())) for _ in range(n)]

c0 = [[False] * 10 for _ in range(n)]
c1 = [[False] * 10 for _ in range(n)]
c2 = [[False] * 10 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] != 0:
            c0[i][a[i][j]] = True
            c1[j][a[i][j]] = True
            c2[(i//3)*3+(j//3)][a[i][j]] = True

solve(0)