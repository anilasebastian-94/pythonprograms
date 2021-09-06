import re
x=input('enter no')
n='[K][L][0-9]{2}[A-Z]{2}[0-9]{4}$'
match=re.fullmatch(n,x)
if match is not None:
    print('valid  no')
else:
    print('invalid  no')