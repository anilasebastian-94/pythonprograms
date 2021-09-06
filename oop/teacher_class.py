class Teacher:
    clg_name='Luminar'
    def __init__(self,tname,sub,tid,dept):
        self.tname=tname
        self.sub=sub
        self.tid=tid
        self.dept=dept
    def printval(self):
        print(self.tname,self.sub,self.tid,self.dept,Teacher.clg_name)
obj=Teacher('Anu','python',123,'online')
obj.printval()