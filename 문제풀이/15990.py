memo = [[0] * 4 for _ in range(100001)]
memo[1] = [0,1,0,0]
memo[2] = [0,0,1,0]
memo[3] = [0,1,1,1]


for i in range(4, 1000001):
    memo[i][1] = (memo[i-1][2] + memo[i-1][3]) % 1000000009
    memo[i][2] = (memo[i-2][1] + memo[i-2][3]) % 1000000009
    memo[i][3] = (memo[i-3][1] + memo[i-3][2]) % 1000000009



t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(memo[n]% 1000000009))