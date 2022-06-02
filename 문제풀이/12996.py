n, a, b, c = map(int,input().split())
d = [[[[-1] * (51) for _ in range(51)] for _ in range(51)] for _ in range(51)]

def solve(n,a,b,c):
    if n == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    
    if a < 0 or b < 0 or c < 0:
        return 0
    if d[n][a][b][c] != -1:
        return d[n][a][b][c]
    
    d[n][a][b][c] = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i + j + k == 0:
                    continue
                d[n][a][b][c] += solve(n - 1, a - i, b - j, c - k)
    d[n][a][b][c] %= 1000000007
    return d[n][a][b][c]

print(solve(n,a,b,c))