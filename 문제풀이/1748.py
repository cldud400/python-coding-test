n = int(input())
m = n
cnt = 0
while m >= 1:
  m /= 10
  cnt += 1

def counter(i):
  if i > 0:
    return (10**i - 10**(i-1)) * (i) + counter(i-1)
  else:
    return 0


def calc(n, x):
  if x > 0:
    return (n - 10**(x-1) + 1) * x + counter(x-1)
  else:
    return 0

print(calc(n, cnt))