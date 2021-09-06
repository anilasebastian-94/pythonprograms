#x='[a-z]'
import re
x='[a-z]'
matcher=re.finditer(x,'Anila mol Sebastian@123456')
for match in matcher:
    print('position:',match.start())
    print('group:',match.group())