a={1,2,3,4,5,6,7,8,9}
prime=set()
non_prime=set()
for i in a:
    if i>1:
        for j in range(2,i):
            if (i%j)== 0 :
                non_prime.add(i)
                break
        else:
            prime.add(i)
print(prime)
print(non_prime)
