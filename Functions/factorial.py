# def factorial(num) :
#     fact=1
#     if num>0 :
#         for i in range(1,num+1) :
#             fact*=i
#         print(fact)
#     elif num==0:
#         print('factorial of zero is 1')
#     else :
#         print('factorial of negative number doesnot exist')
# factorial(5)

#function with return type

def factorial(num) :
    fact=1
    if num>0 :
        for i in range(1,num+1) :
            fact*=i
        return fact
    elif num==0:
        return 'factorial of zero is 1'
    else :
        return'factorial of negative number doesnot exist'
print(factorial(-7))
print(factorial(7))




