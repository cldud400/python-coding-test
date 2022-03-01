def blockLong(arr):
    cnt = 0
    size = len(arr)
    for i in range(n[0]):
        sum = 0
        for j in range(n[1]):
            if j + 3 < n[1] :
                sum = arr[i][j] +  arr[i][j+1] +  arr[i][j+2] +  arr[i][j+3]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        for j in range(n[1]):
            if i + 3 < n[0]:
                sum = arr[i][j] +  arr[i+1][j] +  arr[i+2][j] +  arr[i+3][j]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum

    return cnt

def blockSquare(arr):
    cnt = 0
    size = len(arr)
    for i in range(n[0]):
        sum = 0
        for j in range(n[1]):
            if i + 1 < n[0] and j + 1 < n[1]:
                sum = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum

    return cnt

def blockL(arr):
    cnt = 0
    size = len(arr)
    for i in range(n[0]):
        sum = 0
        # L모양
        for j in range(n[1]):
            if i + 2 < n[0] and j + 1 < n[1]:
                sum = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        # 「 모양
        for j in range(n[1]):
            if i + 1 < n[0] and j + 2 < n[1]:
                sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        # ㄱ 모양
        for j in range(n[1]):
            if i + 2 < n[0] and j + 1 < n[1]:
                sum = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        # 」 모양
        for j in range(n[1]):
            if i + 2 < n[0] and j -1 >= 0:
                sum = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j-1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum

        # 대칭시켜서 」모양
        for j in range(n[1]):
            if i - 1 >= 0 and j + 2 < n[1]:
                sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+2]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        # 대칭시켜서 ㄴ모양 
        for j in range(n[1]):
            if i + 1 < n[0] and j + 2 < n[1]:
                sum = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        # 대칭시켜서 「 모양
        for j in range(n[1]):
            if i + 2 < n[0] and j + 1 < n[1]:
                sum = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i][j+1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum

        # 대칭시켜서 ㄱ모양
        for j in range(n[1]):
            if i + 1 < n[0] and j + 2 < n[1]:
                sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum

    return cnt

def blockStair(arr):
    cnt = 0
    size = len(arr)
    for i in range(n[0]):
        sum = 0

        # 원래모양
        for j in range(n[1]):
            if i + 2 < n[0] and j + 1 < n[1]:
                sum = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        # 시계방향 한번
        for j in range(n[1]):
            if i - 1 >= 0 and j + 2 < n[1]:
                sum = arr[i][j] + arr[i][j+1] + arr[i-1][j+1] + arr[i-1][j+2]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        
        # 대칭시켜서
        for j in range(n[1]):
            if i + 2 < n[0] and j - 1 >= 0:
                sum = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+2][j-1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        
        # 시계방향 한번
        for j in range(n[1]):
            if i + 1 < n[0] and j + 2 < n[1]:
                sum = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum

    return cnt

def blockTable(arr):
    cnt = 0
    size = len(arr)
    for i in range(n[0]):
        sum = 0


        # 원래모양
        for j in range(n[1]):
            if i + 1 < n[0] and j + 2 < n[1]:
                sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum

        # 시계방향 한번
        for j in range(n[1]):
            if i + 2 < n[0] and j - 1 >= 0:
                sum = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j-1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        
        # 시계방향 두번
        for j in range(n[1]):
            if i + 1 < n[0] and j - 1 >= 0 and j + 1 < n[1] :
                sum = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum

        # 시계방향 세번
        for j in range(n[1]):
            if i + 2 < n[0] and j + 1 < n[1]:
                sum = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1]
            else:
                sum = 0
            if cnt < sum:
                cnt = sum
        
    return cnt


n = list(map(int,(input().split())))
arr = list(list(map(int,input().split())) for _ in range(n[0]))

answer = 0
cnt = 0
cnt = blockLong(arr)
if answer < cnt:
    answer = cnt
cnt = blockSquare(arr)
if answer < cnt:
    answer = cnt
cnt = blockL(arr)
if answer < cnt:
    answer = cnt
cnt = blockStair(arr)
if answer < cnt:
    answer = cnt
cnt = blockTable(arr)
if answer < cnt:
    answer = cnt

print(answer)