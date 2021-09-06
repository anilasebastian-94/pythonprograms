import re
x=input('text')
n='[a-z0-9]+[@][g][m][a][i][l][.][c][o][m]$'
match=re.fullmatch(n,x)
if match is not None:
    print('valid  no')
else:
    print('invalid  no')