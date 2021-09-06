
class Student:
    def __init__(self,name,age):  #constructor
        self.name=name
        self.age=age
    def printv(self):
        print('name',self.name)
        print('age',self.age)
    # def __str__(self): #2 string method
    #      return self.name
f1=open('stud', 'r')
for line in f1:
    print(line)
    l=line.split(',')
    print(l)
    name=l[0]
    age=l[1]
    st=Student(name,age)
    st.printv()
