import sys
from collections import deque
from collections import defaultdict
# sys.setrecursionlimit(100000)
t = int(sys.stdin.readline())

for _ in range(t):
    n, m= map(int,sys.stdin.readline().split())
    al = defaultdict(list)

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())

        # 인접 리스트
        al[i].append(j)
        al[j].append(i)



    check = [0] * (n+1)     # 0그룹, 1그룹, 2그룹

    # 인접 리스트(DFS)
    def dfs(x, g):
        check[x] = g    # 그룹
        for i in al[x]:
            if not check[i]:   # 방문한 적이 없으면
                if not dfs(i, 3-g): # 방문한 적이 없는데 다른 그룹이면 X
                    return False
            elif check[i] == check[x]:  # 방문한 적이 있는데 같은 그룹이면 X
                return False
        return True

    ans = True
    for i in range(1, n+1):
        if not check[i]:
            if not dfs(i, 1):
                ans = False

    print('YES' if ans else 'NO')
