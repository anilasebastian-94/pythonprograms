class Person:
    def setvalue(self,name,age):
        self.name=name
        self.age=age
    def printvalue(self):
        print("name",self.name)
        print('age',self.age)
pe1=Person()
pe1.setvalue('Anila',26)
pe1.printvalue()
pe2=Person()
pe2.setvalue('Anu',28)
pe2.printvalue()