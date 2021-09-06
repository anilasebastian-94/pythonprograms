class Person:
    def set(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
        print(self.name,self.age,self.adress)
class Parent:
    def setv(self,childname,std):
        self.childname=childname
        self.std=std
        print(self.childname,self.std)
class Teacher(Person,Parent):
    def printv(self,id,sub):
        self.id=id
        self.sub=sub
        print(self.id,self.sub)
t1=Teacher()
t1.set('anu',26,'abc')
t1.setv('ammu',1)
t1.printv(123,'maths')