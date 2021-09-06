class Person:
    def printval(self,name):
        self.name=name
        print('inside person method',self.name)
class Student(Person):
    def printval(self,dept):
        self.dept=dept
        print('inside student method',self.dept)
st=Student()
st.printval('eng')
st.printval('ani')

#student class overrides person class