from collections import deque
from collections import defaultdict
# sys.setrecursionlimit(1000000)

MAX = 200000
n, k= map(int,input().split())

check = [False] * (MAX +1)
dist = [0] * (MAX + 1)

# check[n] = True
dist[n] = 0

queue0 = deque()
queue0.append(n)
x = n
while x != 0 and x <= k:
  x *= 2
  queue0.append(x)
  check[x] = True
  

queue1 = deque()
queue1.append(n)

while queue0 and queue1:
  now1 = queue0.popleft()
  now2 = queue1.popleft()
  if now2*2 <= MAX:
    queue0.append(now2 * 2)
    dist[now2 * 2] = dist[now2]
    check[now2*2] = True
  if now1 == k or now2 == k:
    break
  for next in [now1-1, now1+1]:
    if 0 <= next <= MAX and check[next]== False:
      check[next] = True
      dist[next] = dist[now1] + 1
      queue1.append(next)

  for next in [now2-1, now2+1]: 
    if 0 <= next <= MAX and check[next] == False:
      check[next] = True
      dist[next] = dist[now2] + 1
      queue1.append(next)
  
print(dist[k])