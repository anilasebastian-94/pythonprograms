import re
x='^a'
r='nila mol sebastian aa aaaa sdasd'
matcher=re.finditer(x,r)
for match in matcher:
    print('position:',match.start())
    print('group:',match.group())