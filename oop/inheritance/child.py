#multiple inheritance
class Person:
    def set(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
        print(self.name,self.age,self.adress)

class Child:
    def setv(self,std,school):
        self.std=std
        self.school=school
        print(self.std,self.school)
class Student(Person,Child):
    def printv(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
st=Student()
st.set('anu',21,'abc')
st.setv(11,'Luminar')
st.printv(2,90)
#parent class.........Person,Child
