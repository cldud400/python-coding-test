n = int(input())
cnt = 0
i = 1
k = 1
while i <= n:
  j = i * 10 - 1
  if j > n: j = n
  cnt += (j - i + 1) * k
  i *= 10
  k += 1
print(cnt)