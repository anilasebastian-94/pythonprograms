# polymorphism...same name different functionality
# overriding....same method name and same no of arguments
# overloading....same method name but diff num of parameters....python doesnot support....only latest method will run
#................................overloading...............................
# class Student:
#     def show(self,num1):
#         self.num1=num1
#         print(self.num1)
#
#     def show(self,num2,num3):
#         self.num2=num2
#         self.num3=num3
#         print(self.num2,self.num3)
# ob=Student()
# ob.show(3,5)
# class Operators:
#     def num(self,n1,n2):
#         self.n1-n1
#         self.n2=n2
#         print(self.n1+self.n2)
#     def num(self,n3):
#         self.n3=n3
#         print(self.n3)
#
# ob=Operators()
# ob.num(5)
#................................overriding......................
class Person:
    def printv(self,name):
        self.name=name
        print('inside parent method',self.name)

class Child(Person):
    def printv(self,class1):
        self.class1=class1
        print('inside child method',self.class1)
ob=Child()
ob.printv('abc')  #...............child class overrides parent class...........