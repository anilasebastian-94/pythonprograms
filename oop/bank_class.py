class Bank:
    bname='SBI'
    def accnt_create(self,acno,name):
        self.acno=acno
        self.name=name
        self.minblnc=10000
        self.blnce=self.minblnc

    def deposit(self,amt):
        self.amt=amt
        self.blnce += self.amt
        print('Your',Bank.bname,'account is credited with amt',self.amt)
        print('Your account balance is',self.blnce)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.blnce:
            print('insufficient balane')
        else:
            print('account is debited with',self.amnt)
            self.blnce-=self.amnt
            print('available balane',self.blnce)
obj=Bank()
num=int(input('enter acno'))
obj.accnt_create(num,'abc')
obj.deposit(10000)
obj.withdraw(5000)






