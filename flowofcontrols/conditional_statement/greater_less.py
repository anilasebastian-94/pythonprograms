# num1=int(input('enter first number'))
# num2=int(input('enter second number'))
#
# if num1>num2:
#     print(num1,'greater than',num2)
# elif num1<num2 :
#     print(num1,'less than',num2)
# else :
#     print('both numbers are equal')

#if condition1 and condition2
    # block content

num1=int(input('enter first number'))
num2=int(input('enter second number'))
num3=int(input('enter third number'))
if num1>num2 and num1>num3:
  print('num1 greater',num1)
elif num2>num1 and num2>num3:
    print('num2 greater',num2)
elif num1==num2==num3 :
    print('equal')
else :
    print('num3 greater',num3)