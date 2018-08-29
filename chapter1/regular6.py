import re
str = "phpPythonPerl"
# findall('表达式'，匹配的字符串，匹配规则)
# 这里的匹配规则是re.I 忽略大小写   re.S  标准的匹配规则 （匹配除换行符以外的所有字符）
res = re.findall('PHP',str,re.I)
print(res)