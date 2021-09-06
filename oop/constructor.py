#constructor is used to initialise instance variables

# class Person:
#     def __init__(self,name,age,adress): #constructor
#         self.name=name
#         self.age=age
#         self.adress=adress
#     def printval(self):
#         print(self.name,self.age,self.adress)
# obj=Person('Anu',26,'abc')
# obj.printval()

#......................................Employee Class........................
class Employee:
    cname='Luminar'
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    def printval(self):
        print(self.name,self.dept,self.salary,Employee.cname)
obj=Employee('Anu','design',25000)
obj.printval()