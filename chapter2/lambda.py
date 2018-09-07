# 闭包返回的是一个对象，主要还是研究作用域的问题
#

def curve_pre():
    a = 25
    def curve(x):
        return a*x*x
    return curve
a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))


#lambda 表达式
f = lambda x,y:x*y
print(f(11,3))

list_x = [1,2,3,4,5,6,7,8,9]
# def squar(x):
#     return x*x

# r = map(squar,list_x)
# lambda 比函数更加简洁
r = map(lambda x:x*x,list_x)
print(list(r))



