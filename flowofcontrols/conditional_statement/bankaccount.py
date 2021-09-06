fixed=10000
withdrawn=int(input('enter amount to be withdrawn'))
if withdrawn<=fixed :
    balance=fixed-withdrawn
    print(balance)
else :
    print('insufficient balance')