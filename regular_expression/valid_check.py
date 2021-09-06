import re
x='56kg'
n='[0-9]{2}[k][g]+'
match=re.fullmatch(n,x)
if match is not None:
    print('valid')
else:
    print('invalid')
