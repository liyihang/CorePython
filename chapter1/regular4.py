import re
# 数量词
#贪婪模式和非贪婪模式
# * 匹配0次或者多次
# + 匹配1次或者多次
# ？匹配0次或者1次

str = "PHPjavaPHP123PHPPython"
# res = re.findall('PHP+',str)
res = re.findall('PHP?',str)
print(res)
