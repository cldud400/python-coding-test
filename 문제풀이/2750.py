import sys


n = int(sys.stdin.readline().rstrip())
sort = []
for _ in range(n):
    m = int(sys.stdin.readline().rstrip())
    if len(sort) == 0:
        sort.append(m)
        continue
    flag = True
    for i in range(len(sort)):
        if sort[i] > m:
            sort.insert(i, m)
            flag = False
            break
    if flag:            # 작은값이 없으면 맨뒤에 추가
        sort.append(m)

for x in sort:
    print(x)