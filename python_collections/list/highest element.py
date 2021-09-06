lst=[1,2,3,4,5,6,7,8,9,55,-44,22,11,33,42,24,62]
b=[]
while lst:
    min=lst[0]#min=1
    for i in lst: #i=1,2
        if i < min:
            min=i
    b.append(min)
    lst.remove(min)
print(b)
print('highest element is:',b[-1])
print('lowest element is:',b[0])
#.......................................with in built function.....................
# lst=[1,2,3,4,5,6,7,8,9,55,44,22,11,33,42,24,62]
# lst.sort()
# print(lst)
# print('highest element is:',lst[-1])
# print('lowest element is:',lst[0])

