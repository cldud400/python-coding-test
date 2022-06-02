# s = input()
# n = len(s)
# d = [[[[[False] * (3) for _ in range(3)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
# # ans = [''] * (n)
# ans = ''
# def solve(i,a,b,c,p1,p2):
#     if (a == 0 and b == 0 and c == 0): return True
    
#     if d[a][b][c][p1][p2]: return False
#     d[a][b][c][p1][p2] = True

#     global ans
#     tmp = ans
#     if a > 0:
#         ans = tmp + 'A'   
#         # ans[i] = 'A'
#         if solve(i+1,a-1, b, c, 0, p1): return True
#     if b > 0 and p1 != 1:
#         ans = tmp + 'B'
#         # ans[i] = 'B'   
#         if solve(i+1,a,b-1,c,1,p1): return True
#     if c > 0 and p1 != 2 and p2 != 2:
#         ans = tmp + 'C'   
#         # ans[i] = 'C'
#         if solve(i+1,a,b,c-1,2,p1): return True
#     return False

    
# a,b,c = 0,0,0

# for i in range(n):
#     if s[i] == 'A': a += 1
#     elif s[i] == 'B': b += 1
#     else: c += 1


# if solve(0,a,b,c,0,0): print(ans)
# else: print(-1)

s = input()
limit = [0,0,0]
n = len(s)
for ch in s:
    limit[ord(ch) - ord('A')] += 1

d = d = [[[[[-1] * (3) for _ in range(3)] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

def solve(a,b,c,p1,p2):
    if a + b + c == n:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if  d[a][b][c][p1][p2] != -1:
        return d[a][b][c][p1][p2]
    if a + 1 <= limit[0] and solve(a+1,b,c,0,p1) == 1:
        d[a][b][c][p1][p2] = 1
        return d[a][b][c][p1][p2]
    if b + 1 <= limit[1] and p1 != 1:
        if solve(a,b+1,c,1,p1) == 1:
            d[a][b][c][p1][p2] = 1
            return d[a][b][c][p1][p2]
    if c + 1 <= limit[2] and p1 != 2 and p2 != 2:
        if solve(a,b,c+1,2,p1) == 1:
            d[a][b][c][p1][p2] = 1
            return d[a][b][c][p1][p2]
    
    d[a][b][c][p1][p2] = 0
    return d[a][b][c][p1][p2]

def trace(a,b,c,p1,p2):
    if a + b + c == n: return ''
    if a + 1 <= limit[0] and solve(a+1,b,c,0,p1) == 1:
        return 'A' + trace(a+1,b,c,0,p1)
    if b + 1 <= limit[1] and p1 != 1:
        if  solve(a,b+1,c,1,p1) == 1:
            return 'B' + trace(a,b+1,c,1,p1)
    if c + 1 <= limit[2] and p1 != 2 and p2 != 2:
        if solve(a,b,c+1,2,p1) == 1:
            return 'C' + trace(a,b,c+1,2,p1)

ret = solve(0,0,0,0,0)
if ret == 0: print(-1)
else: print(trace(0,0,0,0,0))
