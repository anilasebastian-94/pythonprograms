# class Addition:
#     def setvalue(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def printvalue(self):
#         print('sum is:',self.num1+self.num2)
# s1=Addition()
# s1.setvalue(2,5)
# s1.printvalue()
# s2=Addition()
# s2.setvalue(8,5)
# s2.printvalue()
# s3=Addition()
# s3.setvalue(7,4)
# s3.printvalue()

#...................................Alternate method.......................................

class Addition:
    def setvalue(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
a1=Addition()
num1=int(input('enter'))
num2=int(input('enter'))
a1.setvalue(num1,num2)
a2=Addition()
num1=int(input('enter'))
num2=int(input('enter'))
a2.setvalue(num1,num2)