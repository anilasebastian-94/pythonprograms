num=int(input('enter number'))
fact=1
if num>0 :
    for i in range(1,num+1) :
        fact*=i
    print(fact)
elif num == 0:
    print('Factorial of zero is 1')
else :
    print('factorial doesnt exist for negative number')





# i=1
# while i<=num :
#     prdct*=i
#     i+=1
# print(prdct)
