def combination_repetition(r, selected=[]):
    if r == 0:
        for i in numbers:
            # print(' '.join(selected))     # 문자열 리스트로 바꿔서 처리하는 방법
            print(*selected)    # 리스트의 원소를 출력하는 방법
            return
    for i in numbers:
        selected.append(i)
        combination_repetition(r-1, selected)
        selected.pop(-1)

n, m = map(int, input().split())
numbers = list(range(1, n+1))
# numbers = list(map(str, range(1, n+1)))
combination_repetition(m)