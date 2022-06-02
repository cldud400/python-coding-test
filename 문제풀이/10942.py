import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = [[0] * n for _ in range(n)]

t = int(sys.stdin.readline())

# 길이가 1인 경우는 무조건 펠린드롬
for i in range(n):
    d[i][i] = True

# 길이가 2인 경우에는 두 수가 같으면 펠린드롬
for i in range(n-1):
    if a[i] == a[i+1]:
        d[i][i+1] = True

# 길이가 3 이상인 부분수열부터 펠린드롬을 체크
for k in range(3, n+1):
    for i in range(0, n-k+1):
        j = i+k-1
        if a[i] == a[j] and d[i+1][j-1]:
            d[i][j] = True

for _ in range(t):
    s, e = map(int,sys.stdin.readline().split())
    if d[s-1][e-1]:
        print(1)
    else:
        print(0)