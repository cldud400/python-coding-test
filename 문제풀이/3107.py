a = input().split(':')

if len(a) == 9:
    a.remove('')
for i in range(len(a)-1):
    if a[i] == '' and a[i+1] == '':
        for j in range(8-len(a)):
            a.insert(i,'')

    if a[i] == '' and a[i+1] != '':
        for j in range(8-len(a)):
            a.insert(i,'')



for i in range(len(a)):
    if len(a[i]) != 4:
        a[i] = '0' * (4-len(a[i])) + a[i]

print(*a, sep = ':')