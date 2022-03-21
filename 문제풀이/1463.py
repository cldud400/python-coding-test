n = int(input())
memo = memo = [0] * (n+1)

def solve(n):
  if n == 1: return 0
  if memo[n] > 0: return memo[n]

  # 모든 수에 대해서 1을 뺄 수 있다
  memo[n] = solve(n-1) + 1
  if n % 2 == 0:
    tmp = solve(n//2) + 1
    if memo[n] > tmp: memo[n] = tmp

  if n % 3 == 0:
    tmp = solve(n // 3) + 1
    if memo[n] > tmp: memo[n] = tmp

  return memo[n]


print(solve(n))
