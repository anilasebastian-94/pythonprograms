# class Person:
#     def setvalue(self,name1):
#         self.name1=name1
#         print(self.name1)
# class Student(Person):
#     def setvalue(self,name2,name3):
#         self.name2=name2
#         self.name3=name3
#         print(self.name2,self.name3)
# obj=Student()
# obj.setvalue('anila','anu')
# obj.setvalue('anu')

class Operators:
    def num(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1,self.num2)
    def num(self,num3):
        self.num3=num3
        print(self.num3)
op=Operators()
op.num(7)
op.num(4,8)
