def permutation(r, src, selected=[]):
    if r == 0:
        for i in numbers:
            print(*selected)     # 문자열 리스트로 바꿔서 처리하는 방법
            return
    
    size = len(src)
    for i in range(size):
        pick = src.pop(i)
        selected.append(pick)
        permutation(r-1, src, selected)
        selected.pop(-1)
        src.insert(i, pick)


n, m = map(int, input().split())
numbers = list(range(1, n+1))
# numbers = list(map(str, range(1, n+1)))

permutation(m, numbers[:])