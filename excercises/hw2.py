# sum of pairs
lst=[1,3,7,5,6,9,4]
pair=8
# pairs=[]
for i in lst:   # o(n^2)
     for j in lst:
        if(i!=j):
            if(pair==(i+j)):
                print(i,j)
# low=0
# upp=len(lst)-1
# while (low<upp):
#     sum=lst[low]+lst[upp]
#     if sum==pair:
#         pairs.append((lst[low],lst[upp]))
#         low+=1
#     elif sum>pair:
#         upp-=1
#     elif sum<pair:
#         low+=1
# print(pairs)



