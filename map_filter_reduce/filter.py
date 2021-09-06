#print even numbers from list
lst=[2,3,4,5,6]
#filter:filter(function,iterable)
evens=list(filter(lambda num:num%2==0, lst))
print(evens)
odd_numbers=list(filter(lambda num:num%2!=0, lst))
print(odd_numbers)