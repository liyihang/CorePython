import re

s = 'life is short,i use python'
r = re.search('life(.*)python',s)
print(r.group(1))