# 使用re 模块来匹配
import re
a = 'demo|node|captcha|goods'
rest =re.findall('node',a)
# 这里获取的是一个list的数据类型
# print(type(rest))
# 扩展我们如何转成string类型呢
str = (''.join(rest))
print(type(str))