from functools import reduce
lst=[1,2,3,4,5,6]
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)
#find largest
largest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(largest)
#lowest number
lowest=reduce(lambda num1,num2: num1 if num1<num2 else num2, lst)
print(lowest)
