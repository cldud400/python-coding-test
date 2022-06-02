n = int(input())
a = list(input())
m = (n+1)//2 -1
ans = None

for s in range(1<<m):
    ok = True
    for i in range(m-1):
        if (s & (1<<i)) > 0 and (s & (1<<(i+1))) > 0:
            ok = False
    if not ok: continue

    b = a[:]
    #우선순위를 고려해서 계산을 하는것 보다 그냥 괄호 씌워서 직접 계산하면 된다
    for i in range(m):
        if (s & (1<<i)) > 0:
            k = 2 * i + 1
            b[k-1] = '(' + b[k-1]
            b[k+1] = b[k+1] + ')'
    exp = ''.join(b)
    result = eval(exp)

    if ans is None or ans < result: ans = result

print(ans)