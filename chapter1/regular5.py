import re
#边界匹配
# ^开始位置匹配 $末位位置开始匹配
QQ = '123123123'
# res = re.findall('^\d{4,8}$',QQ)
res = re.findall('^123',QQ)
print(res)