# 2 types of variables
#instance variable...related to methods
#static variables...related to class.....accessed using class
# class Student:
#     def setvalue(self,name,clss,rollno,school):
#         self.name=name
#         self.clss=clss
#         self.rollno=rollno
#         self.school=school
#     def printvalue(self):
#         print(self.name,self.clss,self.rollno,self.school)
# st1=Student()
# st1.setvalue('anu',7,24,'depaul')
# st1.printvalue()

class Student:
    school='Luminar'
    def setvalue(self, name, clss, rollno):
        self.name=name
        self.clss=clss
        self.rollno=rollno

    def printvalue(self):
       print(self.name,self.clss,self.rollno,Student.school)
st=Student()
st.setvalue('Anu',2,12)
st.printvalue()
st1=Student()
st1.setvalue('Amal',3,11)
st1.printvalue()
