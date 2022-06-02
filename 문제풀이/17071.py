from collections import deque

n, k = map(int,input().split())

# 홀수시간, 짝수시간 나눠서 생각
d = [[-1]*2 for _ in range(500001)]
if n == k: print(0); exit()
q = deque()
q.append((n,0))
d[n][0] = 0
t = 1

while q:
    x, t = q.popleft()
    for i in [x+1,x-1,x*2]:
        if 0 <= i <= 500000:
            if d[i][1-t] == -1:
                d[i][1-t] = d[x][t] + 1
                q.append((i,1-t))

ans = -1
t = 0
while True:
    k += t
    if k > 500000: break
    if d[k][t%2] <= t:
        ans = t
        break
    t += 1

print(ans)
    