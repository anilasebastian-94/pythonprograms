class Person:
    def set(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
        print(self.name,self.age,self.adress)
class Parent:
    def setv(self,child,std):
        self.child=child
        self.std=std
        print(self.child,self.std)
class Employee(Person,Parent):
    def printv(self,cname,dept):
        self.cname=cname
        self.dept=dept
        print(self.cname,self.dept)
ee=Employee()
ee.set('priya',28,'abc')
ee.setv('anu',1)
ee.printv('aica','design')
