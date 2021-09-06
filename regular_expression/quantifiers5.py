import re
x='a{2,4}'
r='anila mol sebastian aa aaaa sdaaasd'
matcher=re.finditer(x,r)
for match in matcher:
    print('position:',match.start())
    print('group:',match.group())