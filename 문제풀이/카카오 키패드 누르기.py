a = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
b = []
hand = 'right'
tmpl1 = 3
tmpl2 = 0
tmpr1 = 3
tmpr2 = 2
ans = ''
for i in range(len(a)):
    if a[i] == 1:
        b.append([0,0])
    elif a[i] == 2:
        b.append([0,1])
    elif a[i] == 3:
        b.append([0,2])
    elif a[i] == 4:
        b.append([1,0])
    elif a[i] == 5:
        b.append([1,1])
    elif a[i] == 6:
        b.append([1,2])
    elif a[i] == 7:
        b.append([2,0])
    elif a[i] == 8:
        b.append([2,1])
    elif a[i] == 9:
        b.append([2,2])
    elif a[i] == 0:
        b.append([3,1])
        
for x,y in b:
        if (x == 0 and y == 0) or (x == 1 and y == 0) or (x == 2 and y == 0):
            tmpl1 = x
            tmpl2 = y
            ans += 'L'
        elif (x == 0 and y == 2) or (x == 1 and y == 2) or (x == 2 and y == 2):
            tmpr1 = x
            tmpr2 = y
            ans += 'R'
        else:
            if (abs(x-tmpl1) + abs(y-tmpl2)) < (abs(x-tmpr1) + abs(y-tmpr2)):
                tmpl1 = x
                tmpl2 = y
                ans += 'L'
            elif (abs(x-tmpl1) + abs(y-tmpl2)) > (abs(x-tmpr1) + abs(y-tmpr2)):
                tmpr1 = x
                tmpr2 = y
                ans += 'R'
            elif (abs(x-tmpl1) + abs(y-tmpl2)) == (abs(x-tmpr1) + abs(y-tmpr2)):
                if hand == 'right':
                    tmpr1 = x
                    tmpr2 = y
                    ans += 'R'
                elif hand == 'left':
                    tmpl1 = x
                    tmpl2 = y
                    ans += 'L'

print(ans)
