from collections import deque

n, k = map(int,input().split())

d = [-1] * 200000
check = [False] * 200000
cnt = [0] * 200000
q = deque()
q.append(n)
d[n] = 0
check[n] = True
cnt[n] = 1

while q:
    now = q.popleft()
    for next in [now-1, now+1, now * 2]:
        if 0 <= next < 200000:
            if not check[next]:
                q.append(next)
                check[next] = True
                d[next] = d[now] + 1
                cnt[next] = cnt[now]
            elif d[next] == d[now] + 1:
                cnt[next] += cnt[now]

print(d[k])
print(cnt[k])