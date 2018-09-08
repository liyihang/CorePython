# 使用python的字典 代替switch case

day = 2


def get_monday():
    return "monday"


def get_sunday():
    return "sunday"


def get_friday():
    return "friday"


def get_default():
    return "unkown"


switcher = {
    0: get_monday,
    1: get_friday,
    2: get_sunday

}
# get 第一个参数是key 第二个参数是key不存在的时候的默认取值
# 这里传递的都是函数
dayName = switcher.get(day, get_default)()
print(dayName)

# 列表推导式

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 遍历a  再平方
# b = [i * i for i in a]
# b = [i **2 for i in a]
# 条件筛选
b = [i ** 3 for i in a if i % 2 == 0]
# b = [i ** 2 for i in a if i % 2 == 0]
print(b)

# 字典的操作

# key value转换
dic = {
    'name': "jim",
    "age": 18,
    "sex": 'Male'
}

rev = {value:key for key,value in dic.items()}
print(rev)