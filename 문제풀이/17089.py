n, m = map(int,input().split())

# 인접행렬 사용
a = [[False] * (n+1) for _ in range(n+1)]
# 친구 수 확인
f = [0] * (n+1)

for _ in range(m):
    i, j = map(int,input().split())
    a[i][j] = a[j][i] = True
    f[i] += 1
    f[j] += 1


ans = -1
# A, B를 구하고 친구 일 때만 C를 구한다
for i in range(1,n+1):
    for j in range(1,n+1):
        if a[i][j]:
            for k in range(1,n+1):
                if a[i][k] and a[j][k]:
                    ret = f[i] + f[j] + f[k] - 6
                    if ans == -1 or ans > ret:
                        ans = ret

print(ans)
        