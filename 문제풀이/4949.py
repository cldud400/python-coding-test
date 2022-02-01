import sys
while True:     #입력 수의 제한이 없다
    string = sys.stdin.readline().rstrip()     #rstrip: 입력의 오른쪽 공백만 없앤다
    if string == '.':
        break
    stack = []
    flag = True
    for x in string:
        if x == '(' or x == '[':
            stack.append(x)         #리스트 x-1번째에 추가
        elif x == ')' or x == ']':
            if len(stack):          #stack에 원소가 남아있다면
                ch = stack.pop(-1)  #리스트 마지막 원소 제거한다음 비교
                if x == ']' and ch != '[':  # ]일때 ch=[이 아니라면
                    flag = False
                    break
                elif x == ')' and ch != '(':
                    flag = False
                    break
            else:
                flag = False
                break
    if flag and len(stack) == 0:
        print('yes')
    else:
        print('no')