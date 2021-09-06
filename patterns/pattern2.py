n=int(input('enter number of rows'))#5

for i in range(n,0,-1):#i=5,4,3,2,1
    for j in range(i):#j=5,4,3,2,1
        print('*',end=' ')#print 5*,4*,3*,2*,1*
    print()