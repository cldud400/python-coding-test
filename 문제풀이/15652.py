def combination(idx, start, n, m):
    if idx == m:
        print(*selected)
        return
  
    for i in range(start, n+1):
        selected[idx] = i
        combination(idx + 1, i, n, m)
    



n, m = map(int, input().split())
selected = [ 0 for _ in range(m)]

combination(0, 1, n, m)