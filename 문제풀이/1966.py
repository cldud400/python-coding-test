import sys
from collections import deque

t = int(sys.stdin.readline()) #제일 처음 입력

for _ in range(t):
    n, m = list(map(int, sys.stdin.readline().strip().split())) #두번째입력
    order = list(map(int, sys.stdin.readline().strip().split())) #세번째입력
    queue = deque([(x, i) for i, x in enumerate(order)]) # (order[0], 0), (order[1], 1) ... index출력
    #queue = deque([(i, x) for i, x in enumerate(order)]) # (0, order[0]),....
    cnt = 0
    while True:
        if queue[0][0] == max(queue)[0]:
            cnt += 1
            if queue[0][1] == m:
                print(cnt)
                break
            else:
                queue.popleft()
        else:
            queue.rotate(-1)