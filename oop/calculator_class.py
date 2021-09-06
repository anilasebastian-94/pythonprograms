class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(self.num1+self.num2)
    def diff(self):
        print(self.num1-self.num2)
    def mul(self):
        print(self.num1*self.num2)
    def div(self):
        print(self.num1/self.num2)

num1 = float(input('emter a number'))
num2 = float(input('enter a number'))
obj=Calculator(num1,num2)
print('select operation')
print('1.Add\n2.Substraction \n3.Multiply \n4.Division')

while True:

        choice=int(input('enter choice'))
        if choice==1:
            obj.add()
        elif choice==2:
            obj.diff()
        elif choice==3:
            obj.mul()
        elif choice==4:
            obj.div()
        else:
            print('invalid choice')
