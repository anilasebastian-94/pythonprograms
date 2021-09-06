def sum(num1,num2):
    return num1+num2
def diff(num1,num2):
    return num1-num2
def prdct(num1,num2):
    return num1*num2
def divident(num1,num2):
    return num1/num2
print('select operation')
print('1.Add\n2.Substraction \n3.Multiply \n4.Division')

while True:
        num1 = float(input('emter a number'))
        num2 = float(input('enter a number'))
        choice=int(input('enter choice'))
        if choice==1:
                # sum(num1,num2)
            print(sum(num1,num2))
        elif choice==2:
                # diff(num1,num2)
            print(diff(num1,num2))
        elif choice==3:
                # prdct(num1,num2)
            print(prdct(num1,num2))
        elif choice==4:
                # divident(num1,num2)
            print(divident(num1,num2))
        else :
            print('enter valid choice')



