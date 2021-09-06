num=int(input('enter number'))

if num>1:
    for i in range(2,num):

        if num%i==0 :
            print('number is not prime')
            break
    else:
        print('number is  prime')
#..................print not used here because print continously executes in for loop............................#
# num=int(input('enter number'))
# flag=0
# if num>1:
#     for i in range(2,num):
#         if num%i==0 :
#             print('number is not prime')
#             break
#     else:
#         flag=1
# if flag==1:
#     print('number is prime')