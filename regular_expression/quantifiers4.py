import re
x='a{2}'
r='anila mol sebastian aa aaa ssd'
matcher=re.finditer(x,r)
for match in matcher:
    print('position:',match.start())
    print('group:',match.group())