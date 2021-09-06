lst=[2,4,6] #[10,8,6]
lst1=[3,5,7] #[12,10,8]
total1=sum(lst)
print(list(map(lambda num:total1-num,lst)))
# print(total1)
# lst_nw1=[total1-num for num in lst]
# print(lst_nw1)
# for i in range(len(lst)):
#     lst_nw1.append(total1-lst[i])
# print(lst_nw1)

total2=sum(lst1)
lst_nw2=[]
for j in range(len(lst1)):
    lst_nw2.append(total2-lst1[j])
print(lst_nw2)
