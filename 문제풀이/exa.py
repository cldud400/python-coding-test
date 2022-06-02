def insert(a, ar, aa=[]):
    if ar != []:    # 기저조건
        if a <= ar[0]:  
            aa.append(a)
            return aa + ar
        
        else:
            aa.append(ar[0])
            return insert(a, ar[1:], aa)
            
    else:
        aa.append(a)
        return aa


def insertion_sort(list_, sort=[]):
  if list_ != []:    # 기저조건
    print('sort:', sort)
    print('list:', list_)
    return insertion_sort(list_[1:], insert(list_[0], sort))
  else:
    return sort

# insert(5, [1,2,3,6])
print([5, 3, 6])
insertion_sort([5, 3, 6])