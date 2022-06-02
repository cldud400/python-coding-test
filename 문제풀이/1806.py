n, m = 10, 15
a = [5,1,3,5,10,7,4,9,2,8]

# n, m = map(int,input().split())
# a = list(map(int,input().split()))

left, right = 0, 0
ans = 9999999
length = 0
ssum = 0
while True:

  if ssum < m:
    if right == n: break
    ssum += a[right]
    right += 1

  else:
    if left == right: break
    ssum -= a[left]
    left += 1

  
  if ssum > m:
    length = right+1 - left

  if ans > length:
    ans = length


if ans == 9999999:
  ans = 0

  
print(ans)


