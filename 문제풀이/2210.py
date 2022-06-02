di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 현재(i,j)에 있고
# 지금까지 만든 수의 길이 len
# 지금까지 만든 수 num
def solve(i,j,num,len):
    if len == 6:
        ans.add(num)
        return

    for k in range(4):
        ni,nj = i + di[k], j + dj[k]
        if 0 <= ni < 5 and 0 <= nj < 5:
            solve(ni,nj,num*10+a[ni][nj], len+1)



a = [list(map(int,input().split())) for _ in range(5)]

ans = set()

for i in range(5):
    for j in range(5):
        solve(i,j,a[i][j],1)

print(len(ans))