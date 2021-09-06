class Person:
    def __init__(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
    def printv(self):
        print('name',self.name)
        print('age',self.age)
        print('adress',self.adress)
class Employee(Person):
    def __init__(self,id,dept,salary,name,age,adress):
        super().__init__(name,age,adress)
        self.id=id
        self.dept=dept
        self.salary=salary
    def print(self):
        print('id',self.id)
        print('dept',self.dept)
        print('salary',self.salary)
ee=Employee(123,'design',45000,'anu',26,'abc')
ee.printv()
ee.print()
