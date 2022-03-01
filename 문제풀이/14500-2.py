import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
max = 0


blocks = [
  [ [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  [ [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], ],

  [ [2, 0, 0, 0], [2, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  [ [2, 2, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], ],
  [ [2, 2, 2, 0], [0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  [ [0, 2, 0, 0], [0, 2, 0, 0], [2, 2, 0, 0], [0, 0, 0, 0], ],

  [ [0, 0, 3, 0], [3, 3, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  [ [3, 0, 0, 0], [3, 0, 0, 0], [3, 3, 0, 0], [0, 0, 0, 0], ],
  [ [3, 3, 3, 0], [3, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  [ [3, 3, 0, 0], [0, 3, 0, 0], [0, 3, 0, 0], [0, 0, 0, 0], ],

  [ [4, 4, 0, 0], [0, 4, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  [ [0, 4, 0, 0], [4, 4, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0], ],

  [ [0, 5, 5, 0], [5, 5, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  [ [5, 0, 0, 0], [5, 5, 0, 0], [0, 5, 0, 0], [0, 0, 0, 0], ],

  [ [6, 6, 0, 0], [6, 6, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  
  [ [0, 7, 0, 0], [7, 7, 7, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
  [ [7, 0, 0, 0], [7, 7, 0, 0], [7, 0, 0, 0], [0, 0, 0, 0], ],
  [ [0, 7, 0, 0], [7, 7, 0, 0], [0, 7, 0, 0], [0, 0, 0, 0], ],
  [ [7, 7, 7, 0], [0, 7, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ],
]






def calc(arr, b, x, y):
    # 블럭 모양대로 점수를 전부 계산
    # 보드의 경계선과 i, j 위치에 대한 보정
    n = len(arr)
    m = len(arr[0])
    sum = 0

    for i in range(4):
        for j in range(4):
            if b[i][j] != 0:
                nx, ny = x + i, y + j
                if (0 <= nx < n) and (0 <= ny < m):
                    sum += arr[nx][ny]

                else:
                    return -1
    return sum


for i in range(n):
    for j in range(m):
        for block in blocks:
            # 블럭 모양대로 점수를 계산
            ret = calc(arr, block, i, j)
            if max < ret: max = ret

print(max)