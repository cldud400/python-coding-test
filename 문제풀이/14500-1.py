t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [ list(map(int, input().split())) for _ in range(n)]
    max = 0
    for i in range(n):
        for j in range(m):
            # 1자
            if j + 3 < m:
                s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
                if max < s: max = s

            if i + 3 < n:
                s = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
                if max < s: max = s

            # 계단
            if j + 1 < m and i + 2 < n:
                s = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
                if max < s: max = s

            if j + 2 < m and i + 1 < n:
                s = arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i][j+2]
                if max < s: max = s

            # 계단2
            if j + 1 < m and i + 2 < n:
                s = arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j]
                if max < s: max = s

            if j + 2 < m and i + 1 < n:
                s = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
                if max < s: max = s

            # ㄴ자
            if j + 1 < m and i + 2 < n:
                s = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
                if max < s: max = s

            if j + 2 < m and i + 1 < n:
                s = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
                if max < s: max = s

            if j + 2 < m and i + 1 < n:
                s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j]
                if max < s: max = s

            if j + 1 < m and i + 2 < n:
                s = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
                if max < s: max = s

            # ㄱ자 -2
            if j + 1 < m and i + 2 < n:
                s = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j]
                if max < s: max = s

            if j + 2 < m and i + 1 < n:
                s = arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
                if max < s: max = s

            if j + 1 < m and i + 2 < n:
                s = arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1]
                if max < s: max = s

            if j + 2 < m and i + 1 < n:
                s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
                if max < s: max = s

            # ㅁ자
            if j + 1 < m and i + 1 < n:
                s = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
                if max < s: max = s

            # 단상
            if j + 2 < m and i + 1 < n:
                s = arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
                if max < s: max = s

            if j + 1 < m and i + 2 < n:
                s = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j]
                if max < s: max = s

            if j + 1 < m and i + 2 < n:
                s = arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j] + arr[i+2][j+1]
                if max < s: max = s
            
            if j + 2 < m and i + 1 < n:
                s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
                if max < s: max = s

    print(max)

