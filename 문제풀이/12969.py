# N, K = map(int,input().split())
# d = [[[[False] * (N*(N-1)//2 + 1) for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
# ans = [''] * (N+2)


# def solve(n,a,b,k):
#     if n == N: 
#         if K == k: return True
#         else: return False

#     if (d[n][a][b][k]):
#         return False
  
#     d[n][a][b][k] = True
#     ans[n] = 'A'
#     if solve(n+1, a+1, b, k): return True

#     ans[n] = 'B'
#     if solve(n+1, a, b+1, k+a): return True

#     ans[n] = 'C'
#     if solve(n+1, a, b, k+a+b): return True

#     return False




# if solve(0,0,0,0):
#     for i in range(len(ans)):
#         if ans[i] != '':
#             print(ans[i], end = '')
#         else: break
# else:
#     print(-1)

n, k = map(int,input().split())
d = [[[[False] * 436 for _ in range(31)] for _ in range(31)] for _ in range(31)]
ans = ''

def solve(i,a,b,p):
    if i == n:
        if p == k: return True
        else: return False
    
    if d[i][a][b][p]: return False
    d[i][a][b][p] = True
    global ans
    tmp = ans
    ans = tmp + 'A'
    if solve(i+1, a+1, b, p): return True
    ans = tmp + 'B'
    if solve(i+1, a, b+1, p+a): return True
    ans = tmp + 'C'
    if solve(i+1, a, b, p+a+b): return True
    return False

if solve(0,0,0,0):
    print(ans)
else: print(-1)