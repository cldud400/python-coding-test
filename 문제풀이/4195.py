import sys

def find(x):        # 재귀 함수
    if x == parent[x]:  # 기저조건
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def friends(i, j):
    i = find(i)
    j = find(j)

    if i != j:
        parent[j] = i
        number[i] += number[j]

t = int(sys.stdin.readline())

for _ in range(t):
    parent = dict()
    number = dict()

    f = int(sys.stdin.readline())
    for _ in range(f):
        i, j = sys.stdin.readline().rstrip().split()
        if i not in parent:
            parent[i] = i
            number[i] = 1
        if j not in parent:
            parent[j] = j
            number[j] = 1
        friends(i, j)
        print(number[find(i)])