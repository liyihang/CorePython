import re



# 把上述字符串中大于5的数字换成9小于的缓存0
def convert(value):
    matched = value.group()
    if int(matched) >= 5:
        return '9'
    else:
        return '0'

num = "A8L59012H234"
res = re.sub('\d', convert, num)
print(res)
