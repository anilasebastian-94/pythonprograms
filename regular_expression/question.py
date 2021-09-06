#combination of uppercase and lowercase and endwith a number
import re
x=input('text')
n='[a-zA-z]+[0-9]$'
match=re.fullmatch(n,x)
if match is not None:
    print('valid ')
else:
    print('invalid')