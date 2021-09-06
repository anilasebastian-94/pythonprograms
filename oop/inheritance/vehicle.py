class Vehicle:
    def __init__(self,model,regno,color):
        self.model=model
        self.regno=regno
        self.color=color
    def printv(self):
        print('model',self.model)
        print('regno',self.regno)
        print('color',self.color)
    def __str__(self): #2 string method...values return only in string format
        return self.color + self.model


ve=Vehicle('duke','KL065001','black')
ve.printv()
print(ve)
