a={1,2,4,5,6,8}
b=(1,3,4,7,9,6)
common=set()
for i in a:
    # for j in b:
    #     if i==j:
    #         print(i,end=' ') # 2 loops not efficient additional times takes
    if i in b:
        common.add(i)
print(common)