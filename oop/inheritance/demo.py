#single inheritance
class Person: #parent class/base class/upper class
    def walk(self):
        print('Person is walking')
    def read(self):
        print('person is reading')
class Student(Person): #subclass/child class/derived class
    def exam(self):
        print('Student attaending exam')
obj=Person()
obj.walk()
obj.read()
obj1=Student()
obj1.read()
obj1.exam()
