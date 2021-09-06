import re
x=input('enter no')
n='\d{10}'
match=re.fullmatch(n,x)
if match is not None:
    print('valid phone no')
else:
    print('invalid phone no')