s = "one4seveneight"
ans = []
idx = 0
list_ = ''
while idx < len(s):
    if s[idx].isdigit() == False:
        list_ += s[idx]
        idx += 1

    elif s[idx].isdigit() == True:
        ans.append(s[idx])
        idx += 1

    if list_ == 'one':
        ans.append('1')
        list_ = ''
    
    elif list_ == 'two':
        ans.append('2')
        list_ = ''
    elif list_ == 'three':
        ans.append('3')
        list_ = ''
    elif list_ == 'four':
        ans.append('4')
        list_ = ''
    elif list_ == 'five':
        ans.append('5')
        list_ = '' 
    elif list_ == 'six':
        ans.append('6')
        list_ = ''
    elif list_ == 'seven':
        ans.append('7')
        list_ = ''
    elif list_ == 'eight':
        ans.append('8')
        list_ = '' 
    elif list_ == 'nine':
        ans.append('9')
        list_ = ''  
    elif list_ == 'zero':
        ans.append('0')
        list_ = ''    

for i in ans:
    print(int(i), end = '')