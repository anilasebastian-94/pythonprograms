class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printv(self):
        print('name',self.name)
        print('age',self.age)
class Student(Person):
    def __init__(self,roll,std,mark,name,age):
        super().__init__(name,age) #calling constructor of super class
        self.roll=roll
        self.std=std
        self.mark=mark
    def print(self):
        print(self.roll)
        print(self.std)
        print(self.mark)

st=Student(12,2,90,'anu',8)
st.print()
st.printv()