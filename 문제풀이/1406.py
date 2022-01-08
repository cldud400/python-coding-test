import sys
read = sys.stdin.readline().strip()
lstack = list(read)     #lstack는 입력
rstack = []
m = int(sys.stdin.readline())   #입력을 정수로 바꿔서
for _ in range(m):
    cmd, _, value = sys.stdin.readline().strip().partition(' ') #[문자, 공백, 문자]로 바꿔주기
    if cmd == 'L':
        if len(lstack):         #모두 제거돼서 없을 수도 있음 그래서 확인해준다
            rstack.append(lstack.pop(-1))   #lstack의 마지막 원소 빼서 rstack에 추가
    elif cmd == 'D':
        if len(rstack):
            lstack.append(rstack.pop(-1))
    elif cmd == 'B':
        if len(lstack):
            lstack.pop(-1)
    elif cmd == 'P':
        lstack.append(value)    
print(''.join(lstack + rstack[-1::-1]))     #rstack는 뒤에서 부터 출력, 리스트를 문자열로 출력
#join()은 split()의 반대 역할을 한다