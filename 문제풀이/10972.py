from itertools import permutations
import math
n = int(input())
numbers = [x for x in range(1,n+1)]
end = math.factorial(n)
list_ = tuple(map(int, input().split()))
cnt = 0

for perm in permutations(numbers, n):
  cnt += 1
  if perm == list_:
    x = cnt
  
  
  if cnt == x+1:
    print(*perm)
    x = -2
    break

  if cnt == end:
      print(-1)