#parallelogram pattern
n=int(input('enter row'))
k=n
for i in range(n):
    for j in range(k):
        print(end=' ')
    k+=1
    for r in range(n):
        print('*',end=' ')
    print()


