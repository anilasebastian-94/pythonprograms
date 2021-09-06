#.............x='[^abc]'.....except abc............
import re
x='[^abc]'
matcher=re.finditer(x,'anila mol sebastian')
for match in matcher:
    print('position:',match.start())
    print('group:',match.group())