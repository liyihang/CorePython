import re
# re.sub 字符的替换
# 第四个参数代表替换的次数，默认是0，替换所有，2就是替换2次

# re.sub可以传递函数进行处理

def convert(value):
    res = value.group()
    return "!!!!"+res+"!!!!"

program = 'PHPjavagoC++gonodego'
# name = re.sub('go','GOLang',program,2)
name = re.sub('go',convert,program)
# 除此之外，python有系统自带的replace可以进行替换
#
# name = program.replace('go',"GOLang",1)

print(name)