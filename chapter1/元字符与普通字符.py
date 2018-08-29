import re
str = 'as0xq12javaPHPhelloimg***,aad,afd,wrw'
# \d	匹配一个数字字符。等价于 [0-9]。
# \D	匹配一个非数字字符。等价于 [^0-9]。
# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。

# rest = re.findall('\d',str)
# for i in rest:
#     print((''.join(i)))
# print(rest)

rest = re.findall('a[a-f]d',str)
print(rest)
