lst=[1,2,3,4,5,6,3,4,6,4]
l=len(lst)
b=[]
for i in range(l):
    k=i+1
    for j in range(k,l):
        if lst[i]==lst[j] and lst[i] not in b:
            b.append(lst[i])
            lst.remove(lst[i])
            print(lst[i])

#print(b)



