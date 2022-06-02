import sys
from collections import deque
from collections import defaultdict
# sys.setrecursionlimit(1000000)
n, k = map(int, (sys.stdin.readline().split()))

def bfs():
    while queue:
        i = queue.popleft()
        if i == k:
            print(arr[i])
            break

        check[i] = 1
        ni1, ni2, ni3 = i + 1, i - 1, i * 2
        
        if 0 <= ni1 <= 100000 and check[ni1] == 0:
            check[ni1] = 1
            arr[ni1] = arr[i] + 1
            queue.append(ni1)
            path[ni1] = i
        if 0 <= ni2 <= 100000 and check[ni2] == 0:
            check[ni2] = 1
            arr[ni2] = arr[i] + 1
            queue.append(ni2)
            path[ni2] = i

        if 0 <= ni3 <= 100000 and check[ni3] == 0:
            check[ni3] = 1
            arr[ni3] = arr[i] + 1
            queue.append(ni3)
            path[ni3] = i
            


            
# ans = [k]
path = [-1] * 100001
check = [0] * 100001
arr = [0] * 100001
# x = k
queue = deque()
queue.append(n)
bfs()
# while path[x] != -1:
#     ans.append(path[x])
#     x = path[x]
# print(*reversed(ans))

def solve(n, k):
    if n != k:
        solve(n, path[k])
    print(k, end = ' ')
solve(n,k)