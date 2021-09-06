#using temporary variable
num1=5
num2=8
temp=num1
num1=num2
num2=temp
print(num1)
print(num2)
#w/o using temporary variable
num1=20
num2=18
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1)
print(num2)
#assignment
num1=22
num2=28
num1,num2=num2,num1
print(num1)
print(num2)



