def next_permutations(a):
    size = len(a) - 1
    i = size
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0: return False
    j = size
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = size
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def prev_permutations(a):
    size = len(a) - 1
    i = size
    while i > 0 and a[i-1] <= a[i]: # 다음 순열과 반대
        i -= 1
    if i <= 0: return False
    j = size
    while a[j] >= a[i-1]:   # 다음 순열과 반대
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = size
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def check(perm, sign):
    for i in range(len(sign)):
        if sign[i] == '>' and perm[i] < perm[i+1]: return False
    if sign[i] == '<' and perm[i] > perm[i+1]: return False
    return True

k = 2
sign = ['<', '>']
small = [ i for i in range(k+1)]
big = [ 9-i for i in range(k+1)]

while True:
  if check(small, sign): break
  if not next_permutations(small): break

while True:
  if check(big, sign): break
  if not prev_permutations(big): break



print(big)
print(small)
