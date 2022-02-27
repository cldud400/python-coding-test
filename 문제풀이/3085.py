import sys

def checkSubstring(arr):
    size = len(arr)
    cnt = 1
    for i in range(size):
        length = 1
        for j in range(size - 1):
            if arr[i][j] == arr[i][j+1]:
                length += 1
            else:
                length = 1
            if cnt < length:
                cnt = length

        for j in range(size - 1):
            if arr[j][i] == arr[j+1][i]:
                length += 1
            else:
                length = 1
            if cnt < length:
                cnt = length
    # if cnt > size:
    #     cnt = size
    return cnt


n = int(sys.stdin.readline().rstrip())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt = 1

for i in range(n):
    for j in range(n):
        # out of range 주의
        if i + 1 < n:
            # 인접한 행을 바꿔준다
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            # 리스트를 전부 순회하면서 같은 문자열의 최대 길이를 찾는다
            tmp = checkSubstring(arr)
            if cnt < tmp:
                cnt = tmp

            # 변경된 리스트는 다시 원래대로
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
        if j + 1 < n:
            # 인접한 열을 바꿔준다
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]


            # 리스트를 전부 순회하면서 같은 문자열의 최대 길이를 찾는다
            tmp = checkSubstring(arr)
            if cnt < tmp:
                cnt = tmp

            # 변경된 리스트는 다시 원래대로
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

print (cnt)

