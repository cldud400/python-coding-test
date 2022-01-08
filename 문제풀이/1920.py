import sys
n = int(sys.stdin.readline())
nList = set(map(int, sys.stdin.readline().rstrip().split()))  #중복을 제거하기 위해 set 사용
m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().rstrip().split()))


for x in mList:
    if x in nList: print(1)
    else : print(0)
