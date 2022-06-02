a, b = map(int,input().split())

# cnt = 0
# while True:
#     if b % 2 == 0:
#         b /= 2
#     else:
#         b -= 1
#         b /= 10
#     cnt += 1
#     if b <= a:
#         break


# if a == b: print(cnt+1)
# else: print(-1)


# def solve(a,b):
#     if a == b: return 1
#     if a > b: return -1

#     d1 = solve(a * 2, b)
#     d2 = solve(a * 10 + 1,b)
#     if d1 == -1 and d2 == -1: return -1
#     if d1 == -1: return d2 + 1
#     if d2 == -1: return d1 + 1
#     return min(d1,d2) + 1

# print(solve(a,b))


i = 1
while a <= b:
    if a == b: print(i+1); exit()
    if b % 10 == 1:
        b = (b-1) // 10
    elif b % 2 == 0:
        b = b // 2
    else: print(-1); break
    i += 1
print(-1)


