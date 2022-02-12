import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    # 나누어 떨어지는 경우 즉, x, y가 0이되는 경우가 존재
    # 범위를 0 <= x,y <= M-1, N-1
    x -= 1
    y -= 1

    k = x

    while k < m*n:
        if k % n == y:
            print(k+1)
            break
        
        k += m
    
    else:
        print(-1)
