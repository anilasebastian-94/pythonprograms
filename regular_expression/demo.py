#re - package for pattern matching
# package collection of modules

import re
count=0
matcher=re.finditer('ab', 'abbababcabbabbbbbabbb')
for match in matcher:
    print('match found position:',match.start())
    print('group',match.group())
    count+=1
print(count)