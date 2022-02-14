import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
fail = sys.stdin.readline().split()
button = [x for x in range(10)]
for x in fail:
  button.remove(int(x))

def checkNumber(n):
  strs = str(n)
  cnt = 0
  for number in strs:
    if int(number) not in button:
      return False
    cnt += 1
  return cnt

cnt = abs(100 - n)
for num in range(1000001):
  ret = checkNumber(num)
  if ret:
    if cnt > ret + abs(n-num):
      cnt = ret + abs(n-num)

print(cnt)