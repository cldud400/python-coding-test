from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# di = [1,1,-1,-1]
# dj = [1,-1,1,-1]
# def check(a):
#     for i in range(5):
#         for j in range(4):
#             for k in range(j+1,5):
#                 if a[i][j] == 'P' and a[i][k] == 'P':
#                     if k - j <= 2:
#                         if a[i][j+1] != 'X':
#                             return False
#                 if a[j][i] == 'P' and a[k][i] == 'P':
#                     if k - j <= 2:
#                         if a[j+1][i] != 'X':
#                             return False
                        
#         for p in range(5):
#             for q in range(5):
#                 for k in range(4):
#                     nx = p + dx[k]
#                     ny = q + dy[k]
#                     ni = p + di[k]
#                     nj = q + dj[k]
#                     if 0 <= ni < 5 and 0 <= nj < 5:
#                         if a[p][q] == 'P' and a[ni][nj] == 'P':
#                             if 0 <= abs(nx-ni) <= 1 and  0 <= abs(ny-nj) <= 1:
#                                 if 0 <= nx < 5 and 0 <= ny < 5:
#                                     if a[nx][ny] != 'X':
#                                         return False
                            
                        
#     return True



a = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]




            
def solve(a,i,j):
    d = [[-1] * 5 for _ in range(5)]
    q = deque()
    d[i][j] = 0
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and d[nx][ny] == -1:
                if a[nx][ny] != 'X':
                    q.append((nx,ny))
                    d[nx][ny] = d[x][y] + 1

    return d




def solution(a):
    ans = [0,0,0,0,0]
    for s in range(5):
        list_ = []
        for i in range(5):
            for j in range(5):
                if a[s][i][j] == 'P':
                    list_.append((i,j))
        flag = True
        for address1 in list_:
            d = solve(a[s],address1[0],address1[1])
            for address2 in list_:
                if address1 != address2:
                    x = address2[0]
                    y = address2[1]

                    if -1 < d[x][y] <= 2:
                        flag = False
                        break
            
            if not flag: break

        if flag: ans[s] = 1
        else: ans[s] = 0
    print(ans)
        
solution(a)





