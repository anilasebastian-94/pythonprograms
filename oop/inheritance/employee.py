class Person:
    def setval(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.adress)
class Employee(Person):
    def set(self,dept,id):
        self.dept=dept
        self.id=id
    def print(self):
        print(self.dept,self.id)
obj=Person()
obj.setval('Anila',26,'abc')
obj.printval()
obj1=Employee()
obj1.setval('Anila',26,'abc')
obj1.printval()
obj1.set(1,123)
obj1.print()
