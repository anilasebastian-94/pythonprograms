n=int(input('enter row'))
r=n
for i in range(n):#[0],[1]
    for j in range(r):#[0,1,2,3,4],[0,1,2,3]
        print(end=' ')
    r-=1 #[4]
    for k in range(i+1):#[0]
        print('*',end=' ')
    print()
