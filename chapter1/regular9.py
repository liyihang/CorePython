import re
s = 'Ah91230J9012K'
# match 从首字母开始匹配 不符合返回none
#search 全局匹配，匹配成功后停止匹配。返回匹配后的结果
#findall 匹配所有
r = re.match('\d',s)
print(r)
r1 = re.search('\d',s)
print(r1.group())