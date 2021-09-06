class Parent:
    def __init__(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
    def printv(self):
        print(self.name,self.age,self.adress)
class Teacher(Parent):
    def __init__(self,dept,id,name,age,adress):
        super().__init__(name,age,adress)
        self.dept=dept
        self.id=id
    def print(self):
        print(self.dept,self.id)
    def __str__(self):
        return str(self.id)+' '+self.name
st=Teacher('python',123,'anu',26,'abc')
st.printv()
st.print()
print(st)