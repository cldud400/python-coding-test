n = int(input())

a = []
for i in range(1,n+1):
  cnt = 0
  for j in range(1,n+1):
    if i % j == 0:
      cnt += 1

  if cnt == 2:
    a.append(i)


left, right = 0, 0
cnt = 0
ssum = 0
while True:

  if ssum < n:
    if right == len(a): break
    ssum += a[right]
    right += 1

  else:
    if left == right: break
    ssum -= a[left]
    left += 1

  
  if ssum == n:
    cnt += 1


print(cnt)
