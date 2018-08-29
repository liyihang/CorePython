import re


str = "java6887python&*PHP\t\n"
# \d匹配数字
# res = re.findall('\d{2,4}',str)
# \D匹配非数字
# res = re.findall('\D{2,4}',str)
# \w匹配单词字符
# res = re.findall('\w{2,4}',str)
# \W匹配非单词字符
# res = re.findall('\W{2,4}',str)
#\s匹配任何空白字符，包括空格、制表符、换页符等等
# res = re.findall('\s{2,4}',str)
#\S匹配任何非空白字符，包括空格、制表符、换页符等等
res = re.findall('\S{2,4}',str)
print(res)
