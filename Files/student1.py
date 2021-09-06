class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printv(self):
        print('name:',self.name)
        print('rollno:',self.rollno)
        print('course:',self.course)
        print('mark:',self.course)
f1=open('stud1','r')
for line in f1:
    l=line.split(',')
    name=l[0]
    rollno=l[1]
    course=l[2]
    mark=l[3]
    st=Student(name,rollno,course,mark)
    st.printv()