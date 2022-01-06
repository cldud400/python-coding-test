import sys
from collections import deque
n = int(sys.stdin.readline())
queue = [x for x in range(1, n+1)]
queue = deque(queue)

for _ in range( len(queue) -1):
    queue.popleft()  #제일 첫번째 원소 꺼내고 제거
    queue.rotate(-1) #음수면 제일 첫번째 원소가 마지막으로 양수면 마지막 원소가 처음으로
print(queue.popleft())
