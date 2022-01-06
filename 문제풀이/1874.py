import sys
n = int(sys.stdin.readline())
stack = []
ans = []
cnt = 1
for _ in range(n):
    m = int(sys.stdin.readline()) #한줄에 하나씩 입력받아서 int로 변환
    while cnt <= m:
        stack.append(cnt)       #입력받은 값까지 stack에 쌓는다
        ans.append('+')
        cnt += 1

    if stack[-1] == m:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        sys.exit(0)

print('\n'.join(ans))