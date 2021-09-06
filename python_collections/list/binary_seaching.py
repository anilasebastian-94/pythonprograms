lst=[1,2,3,4,5,6]
def bsearch():
    lst.sort()
    ele=int(input('enter element'))
    flag=0
    low=0
    upp=len(lst)-1
    while low <= upp:
        mid = (low + upp)// 2

        if ele > lst[mid]:
            low = mid + 1

        elif ele < lst[mid]:
            upp = mid-1
        elif ele == lst[mid]:
            flag = 1
            break
    if flag == 1:
        print('element found')
    else:
        print('element not found')

bsearch()