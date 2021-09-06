a={1,2,3,4,5,6,7,8,9,10.12,15,17,44,58,66,27,83,95,96,22}
odd=set()
even=set()
for i in a:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(a)
print('set of odd numbers is:',odd)
print('set of even numbers is:',even)