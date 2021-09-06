#count including zero number of a
import re
x='a'
r='anila mol sebastian aa aaaa sdasd'
count=0
matcher=re.finditer(x,r)
for match in matcher:
    print('position:',match.start())
    print('group:',match.group())
