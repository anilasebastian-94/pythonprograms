lst=[1,2,3,4]
lst1=[4,5,6,7,8,9]
# def linear_search(lst):
#     a=int(input('enter the element'))
#     for i in lst:
#         if a == i:
#             print('element present')
#             break
#     else:
#         print('not present')
# linear_search(lst)
# linear_search(lst1)

def linear_search(lst):        #........................as per linear search algorithm.......................
    a=int(input('enter the element'))
    flag=0
    for i in lst:
        if a == i:
            flag=1
            break
    if flag==0:
        print('not present')
    else:
        print('element present')
linear_search(lst)