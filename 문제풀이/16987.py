n = int(input())

a = [0] * n
w = [0] * n

for i in range(n):
    a[i], w[i] = map(int,input().split())

def solve(idx):
    # 깨뜨릴 계란을 선택
    # n개의 계란이 선택이 됐으면, 다 깨보면서 확인
    if idx == n:
        cnt = 0
        for i in range(n):
            if a[i] <= 0: cnt += 1
        return cnt
    # 계란이 깨졌거나, 깨지지 않은 다른 계란이 없으면 넘어간다
    if a[idx] <= 0: return solve(idx+1)
    
    ans = 0
    flag = False
    for j in range(n):
        i = idx
        if i == j: continue

        # 깨지지 않은 계란
        if a[j] > 0:
            flag = True
            a[i] -= w[j]
            a[j] -= w[i]
            ret = solve(idx+1)
            if ans < ret: ans = ret
            # 확인 했으면 원복
            a[i] += w[j]
            a[j] += w[i]

    if not flag: return solve(idx+1)
    return ans

print(solve(0))
