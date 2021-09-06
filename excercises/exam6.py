def sum_of_prime(num1,num2):
    res=0
    for a in range(num1,num2):
        if a>1:
            for i in range(2,a):
                if a%i==0:
                    break
            else:
                res+=a
    return res

print('Sum of prime numbers with in given range is:',sum_of_prime(1,50))



