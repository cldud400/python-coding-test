n = int(input())
ans = list(map(int,input().split()))
check = [False]* (n*100000)
def solve(i,s):

  if i == n:
    check[s] = True
    ans.append(s)
    return
  
  solve(i+1, s + ans[i])
  solve(i+1, s)



solve(0,0)
# ans.sort()
# for j in range(0, n*100000):
#   if j not in ans:
#     print(j)
#     break

for i in range(1, len(check)):
  if check[i] == False:
    break


print(i)
    
