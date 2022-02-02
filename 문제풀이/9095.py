n = int(input())

def sumNumber(n):
    if n == 1:   return 1
    elif n == 2: return 2
    elif n == 3: return 4
    else:
        return sumNumber(n-1) + sumNumber(n-2) + sumNumber(n-3)

for i in range(n):
    num = int(input())
    print(sumNumber(num))
    
    
