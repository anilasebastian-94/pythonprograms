#count a as each including 0 number of a
import re
x='a?'
r='anila mol sebastian aa aaaa sdasd'
matcher=re.finditer(x,r)
for match in matcher:
    print('position:',match.start())
    print('group:',match.group())