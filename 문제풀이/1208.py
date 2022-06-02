# n, m = map(int,input().split())
# a = list(map(int,input().split()))

n, s = 5,0 
a = [-7, -3, -2, 5, 8]
m = n // 2
n = n - m

up = [0] * (1<<n)
for i in range(1<<n):
  for k in range(n):
    if  (i& (1<<k)) > 0:
      up[i] += a[k]

down = [0] * (1<<m)
for i in range(1<<m):
  for k in range(m):
    if (i& (1<<k)) > 0:
      down[i] += a[k+n]



up.sort()
down.sort()
down.reverse()


n = (1<<n)
m = (1<<m)
i = j = ans = 0

while i < n and j < m:
  if up[i] + down[j] == s:
    c1 = 1
    c2 = 1
    i += 1
    j += 1
    while i < n and up[i] == up[i-1]: # 같은 합이 있다면
      c1 += 1
      i += 1
    while j < m and down[j] == down[j-1]: # 같은 합이 있다면
      c2 += 1
      j += 1
    ans += c1 * c2

  elif up[i] + down[j] < s: i += 1
  else: j += 1


# 0+0의 경우는 빼준다
if s == 0:
  ans -= 1

print(ans)