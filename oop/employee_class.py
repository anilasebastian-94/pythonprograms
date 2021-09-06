class Employee:
    def setvalue(self,name,age,dept,salary,company):
        self.name=name
        self.age=age
        self.dept=dept
        self.salary=salary
        self.company=company
    def printvalue(self):
        print('name',self.name)
        print('age',self.age)
        print('dept',self.dept)
        print('salary',self.salary)
        print('company',self.company)
e1=Employee()
e1.setvalue('Anila',26,'design',22000,'AICA')
e1.printvalue()
e2=Employee()
e2.setvalue('Alfa',26,'admin',22000,'AICA')
e2.printvalue()