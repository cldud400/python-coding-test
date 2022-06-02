n = int(input())
a = list(map(int,input().split()))
c = max(a)
for i in range(n):
  a[i] = bin(a[i])

cnt = 0

for i in a:
  b = list(i)
  for j in range(len(b)):
    if b[j] == '1':
      cnt += 1
c = bin(c)
print(len(c) - 3 + cnt)