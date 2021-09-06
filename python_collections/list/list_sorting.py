lst=[1,2,3,4,5,6,-99,45,56,89,75,85,96]
sorted_lst=[]
while lst: #1
    min=lst[0]#min= 1,2
    for i in lst: #i=1,2,3,4,5,6,-99
        if i < min:
            min = i
    sorted_lst.append(min)#[1,
    lst.remove(min)
print(sorted_lst)


