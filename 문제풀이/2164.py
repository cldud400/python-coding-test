import sys
from collections import deque
n = int(sys.stdin.readline()) #갯수 입력
queue = deque()
for x in range(1, n + 1):
    # queue.insert(0, x)
    queue.appendleft(x)

for _ in range(n):
    if len(queue) > 1:
        queue.pop()         #deque를 사용 안하면 queue.pop(-1)
        queue.insert(0, queue[-1])
        queue.pop()

print(int(queue[0]))