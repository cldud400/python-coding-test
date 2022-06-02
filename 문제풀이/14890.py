# n, l = 6, 2

# arr = [[3,3,3,3,3,3],[2,3,3,3,3,3],[2,2,2,3,2,3],[1,1,1,2,2,2],[1,1,1,3,3,1],[1,1,2,3,3,2]]
n , l = map(int,input().split())

map = [list(map(int, list(input().split()))) for _ in range(n)]


def go(arr, l):
    n = len(arr)
    check = [False] * n # 이미 경사로를 놓은 곳은 또 놓을 수 없다.
    for i in range(1,n):
        if arr[i-1] != arr[i]: # 경사진 곳(높이 차이가 1보다 크면 안된다)
            diff = abs(arr[i] - arr[i-1])
            if diff != 1:
                return False
            if arr[i-1] < arr[i]: # 높이가 1이라면 l만큼 경사로를 놓을 수 있는지 확인
                for j in range(l, l+1):
                    if i-j < 0: # 짧기 때문에 못 지나간다.
                        return False
                    if arr[i-1] != arr[i-j]:  # 높이가 다른 곳은 경사로를 놓을 수 없다
                        return False
                    if check[i-j]:  # 이전에 경사로를 놓았던 곳은 놓을 수 없다.
                        return False
                    check[i-j] = True

            else:
                for j in range(l):
                    if i+j >= n:
                        return False
                    if arr[i] != arr[i+j]:
                        return False
                    if check[i+j]:
                        return False
                    check[i+j] = True

    return True


ans = 0

# 모든 행을 지나갈 수 있는지 확인
for i in range(n):
  d= map[i]
  if go(d,l):
    ans += 1

# 모든 열을 지나갈 수 있는지 확인
for j in range(n):
  d = [map[i][j] for i in range(n)]
  if go(d,l):
    ans += 1

print(ans)
