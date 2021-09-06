class Student:
    clname = "ABC"
    def __init__(self,name,roll,dep):
        self.name=name
        self.roll=roll
        self.dep=dep
    def printv(self):
        print(self.name)
        print(self.roll)
        print(self.dep)
        print(Student.clname)
    def __str__(self):
        return self.name + str(self.roll)
st=Student('anu',12,'comp')
st.printv()
print(st)
