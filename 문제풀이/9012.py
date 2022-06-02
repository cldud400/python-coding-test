import sys
t = int(sys.stdin.readline())
for _ in range(t):
    braket = sys.stdin.readline().strip()     #strip를 해주는 이유 : readline()를 하면 맨뒤에 \n이 포함되기 때문
    stack = []
    flag = True
    for x in braket:
        if x == '(':
            stack.append(1)
        else:
            if len(stack):
                stack.pop(-1)
            else:
                flag = False
                break
    if flag and len(stack) == 0:
        print('YES')
    else:
        print('NO')