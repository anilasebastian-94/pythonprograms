import re
x='$'
r='anila mol sebastian aa aaaa sdasda'
matcher=re.finditer(x,r)
for match in matcher:
    print('position:',match.start())
    print('group:',match.group())