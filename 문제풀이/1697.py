import sys
from collections import deque
from collections import defaultdict
# sys.setrecursionlimit(100000)
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
        if 0 <= ni2 <= 100000 and check[ni2] == 0:
            check[ni2] = 1
            arr[ni2] = arr[i] + 1
            queue.append(ni2)
        if 0 <= ni3 <= 100000 and check[ni3] == 0:
            check[ni3] = 1
            arr[ni3] = arr[i] + 1
            queue.append(ni3)

            
            

check = [0] * 100001
arr = [0] * 100001
queue = deque()
queue.append(n)
bfs()