def factorial(x): #6

    if x==0:
        return 1
    else :
        return x * factorial(x-1)  #6*5*4*3*2


num=int(input('enter number'))
print('factorial of',num,'is',factorial(num))