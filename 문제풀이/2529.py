# def check(strs):
#     for i in range(k):
#         if signs[i] == '>':
#             if strs[i] < strs[i+1]: return False

#         else:
#             if strs[i] > strs[i+1]: return False

#     return True
# def isTrue(i,j,sign):
#   if sign == '>':
#     if i < j: return False
#   else:
#     if i > j: return False
#   return True

# def solve(i=0, strs=''):
#   if i == k+1:  
#     if check(strs): ans.append(strs)

#     return

#   for x in range(10):
#     if choice[x]: continue
#     if i == 0 or isTrue(strs[i-1], str(x), signs[i-1]):
#       choice[x] = True
#       solve(i+1, strs + str(x))
#       choice[x] = False

# import sys
# ans = []
# k = int(sys.stdin.readline())
# signs = list(map(str, sys.stdin.readline().rstrip().split()))
# # numbers = [x for x in range(10)]
# choice = [False] * 10
# solve()
# ans.sort()
# print(ans[-1])
# print(ans[0])


def check(strs):
    for i in range(k):
      if signs[i] == '>':
        if combi[i] < combi[i+1]: return False

      else:
        if combi[i] > combi[i+1]: return False

      return True

import sys
from itertools import permutations
ans = []
k = int(sys.stdin.readline())
signs = list(map(str, sys.stdin.readline().rstrip().split()))
numbers = [0,1,2,3,4,5,6,7,8,9]


for combi in permutations(numbers, k+1):
  if check(combi): ans.append(combi)

ans.sort()
print(''.join(map(str,ans[-1])))
print(''.join(map(str,ans[0])))

