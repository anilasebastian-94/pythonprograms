lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
b=[]
[b.append(i) for i in lst if i not in b]
print(b)
# print(lst)
# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# b=[]
# for i in lst:
#     if i not in b:
#         b.append(i)
# print(b)
