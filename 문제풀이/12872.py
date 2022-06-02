n, m, s = map(int,input().split())
d = [[-1] * 101 for _ in range(101)]

def solve(p,x,y):
    if p == s:
        if y == 0:
            return 1
        else:
            return 0

    if x > n or y < 0:
        return 0
    if d[p][x] != -1:
        return d[p][x]
    d[p][x] = 0

    if y > 0:
        d[p][x] += solve(p+1,x+1,y-1) * (n-x)
        
    if x > m:
        d[p][x] += solve(p+1,x,y) * (x-m)

    d[p][x] %= 1000000007
    return d[p][x]
    
print(solve(0,0,n))