def pattern():
#     n=int(input('enter number of rows'))
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end=' ')
#         print()
# pattern()
        n = int(input('enter number of rows'))  # 5
        for i in range(n):  # i=0,1,2,3,4,5
            num = 1
            for j in range(i):# j=0,1,2,3.4
                print(num, end=' ')
                num += 1
            print('\r')
pattern()