# **Python入门及进阶**

 

 

​															Author：lidoudou 

​															Email：[lidoudoou@gmail.com](mailto:lidoudoou@gmail.com)                                          	

 

##一.Python发展历史，特性及现状

### 1.Python发展历史

Python是一门面向对象的解释性语言，由Guido van Rossum在1989年发明，并在1991年发布了第一个版本。

Python的版本目前分为2.x版本和3.x版本，两者的区别比较大，主要在类库支持方面和某些语法方面。由于2.x的版本将在2020年停止支持和维护，所以初学者我们建议使用3.x版本，目前最新的版本为3.6.x。

### 2. Python的语言特性

#### 2.1. 简单易学，上手快

Python是一种代表简单主义思想的语言。能够很快的理解语言和极快使用它完成工作。

#### 2.2免费开源

Python是FLOSS（自由/开放源码软件）之一。使用者可以自由地发布这个软件的拷贝、阅读它的源代码、对它做改动、把它的一部分用于新的自由软件中。FLOSS是基于一个团体分享知识的概念。

#### 2.3跨平台，可移植

由于它的开源本质，Python已经被移植在许多平台上（经过改动使它能够工作在不同平台上）。这些平台包括Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、Palm OS、QNX、VMS、Psion、Acom RISC OS、VxWorks、PlayStation、Sharp Zaurus、Windows CE、PocketPC、Symbian以及Google基于linux开发的android平台。

#### 2. 4面向对象

Python既支持面向过程的编程也支持面向对象的编程。在“面向过程”的语言中，程序是由过程或仅仅是可重用代码的函数构建起来的。在“面向对象”的语言中，程序是由数据和功能组合而成的对象构建起来的。不进如此，python还是面向切片和函数式编程。但又有一句话是在Python中everything is abject。

所有说Python是面向工资的语言。

#### 3.5丰富的扩展库

Python标准库确实很庞大。它可以帮助处理各种工作，包括正则表达式、文档生成、单元测试、线程、数据库、网页浏览器、CGI、FTP、电子邮件、XML、XML-RPC、HTML、WAV文件、密码系统、GUI（图形用户界面）、Tk和其他与系统有关的操作。这被称作Python的“功能齐全”理念。除了标准库以外，还有许多其他高质量的库，如wxPython、Twisted和Python图像库等等。

### 3.Python的前景







##二.python基础

### 1. python的变量

### 2. python的基础数据类型

### 3. python的循环

###4. python函数

### 5. python数据结构





## 三.python面向对象



### 1.python的类与对象

#### 1.1 python的类

**类就是现实世界或者思维世界的实体在计算机世界的反应，它将数据和数据上的操作封装在一起。**

示例：

```python
class Student:
    name = 'jim'
    age = 0
    def getInfo(self):
        print('this is a student info')
info = Student()
info.getInfo()

```

上图我们定义了一个student类  类中定一个getInfo()的方法。通过实例化student类，我们得到了info实例，或者说叫做info对象。info对象调用getInfo()方法输出相关信息/返回相关信息。

#### 1.2 python的对象

对象就是具有类属性和方法的具体事物（就是基于类而创建的一个具体的事物），python中一切皆对象。

对象由类产生，上图中的info对象就是由student类产生的。

#### 1.3类变量和实例变量

**在类内部  直接通过变量名定义的为类变量**

**在类或者方法的内部通过self.变量名来定义的变量称为实例变量**

```python
class Student:
    name = 'jim'
    age = 0
    def getInfo(self,name,age):
        self.name = name
        self.age = age
        print(self.name)#这里访问的是实例变量name
        print(self.age)
        print(Student.name)#这里访问的是类变量
        print(Student.__class__.name)#同上

info = Student()
info.getInfo('tom',20)
```

在上面的示例中，我们在student类内部定义的name和age变量为类变量，在getInfo()方法中通过self.name来定义的变量称为实例变量。

#### 1.4 python方法中的self

> 为什么方法的第一个参数是self呢？
> 类(class)初始化之后会得到实例(instance)。self就是用于代表初始化的到的实例。
> 明确地写一个self参数，使得类的方法(method)和普通的函数(function)本质上没有差异，所有的输入参数都显示地传递到方法/函数当中。
> python 的设计原则  是Explicit is better than implicit   显示（暴露）胜于隐藏



#### 1.5 实例方法和类方法和静态方法

**实例方法**需要将类实例化后调用，如果使用类直接调用实例方法,需要显式地将实例作为参数传入。 

**类方法**是通过@classmethod装饰器来声明的方法，此方法可以通过实例或者类直接调用。

**静态方法**是指类中无需实例参与即可调用的方法(不需要self参数)，在调用过程中，无需将类实例化，直接在类之后使用.号运算符调用方法。 

通常静态方法通过@staticmethod装饰器来声明。

示例：

```python
class Student():

    #构造方法
    def __init__(self):
        print('init method')

    # 普通实例方法
    def getInfo(self):
        print( "this is instance func")
    #类方法
    @classmethod
    def getOneInfo(cls):
        print('this is a class method')
    #静态方法
    @staticmethod
    def getTwoInfo():
        print('this is a static method')
# 实例对象可以调用实例方法，类方法和静态方法
obj = Student()
obj.getInfo()
obj.getOneInfo()
obj.getTwoInfo()

# 类可以调用实例方法，类方法和静态方法
Student.getTwoInfo()
Student.getOneInfo()
Student.getInfo()  #此处加上参数即可  不加会有类型错误
```



### 2.python的构造函数

构造方法用于初始化类内部状态的方法，python提供了__init__()方法 .

此方法在类被实例化的时候自动执行，所以一些需要初始化的熟悉就可以放在构造函8数中。

实例：

```python
class Student:
    name = 'jimmy'
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name)
        print(age)
    def getInfo(self,name,age):
        self.name = name
        self.age = age
        print(name)
        print(age)


info = Student('hello',21)#系统会自动执行构造方法，输出hello 21
obj = Student
print(obj.name)#此处输出的是类常量jimmy

```

### 3. python的访问控制（成员可见性）

Python设置 成员变量和方法 为私有的为私有的方式为 **在变量名之前加两个下划线__**  但是被设为私有属性的成员还是方法都可以在类的外部强制调用。

```python
class Stu():
    def __init__(self, name, score):
        # 定义私有属性__score
        self.name = name
        self.__score = score
    # 定义私有方法__getInfo
    def __getInfo(self):
        print(self.__score)
    def homework(self):
        print('do homework')
obj = Stu('lilei', 90)
# 这里我们访问了__score  内部的私有属性  为什么会访问到呢？
obj.__score = 99
# 正常输出99
print(obj.__score)
# 因为python是一门动态语言，这里__score不是我们init方法中定义的的__score而是动态添加的
obj.homework()
print(obj.__dict__)
```

那我们怎么知道此时类内部的__score有两个呢？

我们可以通过__dict__来获取整个类内部的属性和方法来查看上面的验证。

```python
print(obj.__dict__)
```

```
C:\Users\Administrator.ZXW-20170702ZMN\Anaconda3\python.exe H:/Python_demo/obj/private&public.py
99
do homework
{'name': 'lilei', '_Stu__score': 90, '__score': 99}

Process finished with exit code 0
```

这里我们可以看到‘obj.______dict______打印出了属性有name，________Stu______score,______score这里是不是已经有两个了？

类内部的私有属性被转义成了_____Stu______score,我们如果在外部直接访问______score会报错的，之所以没有报错，是因为我们自己动态添加了______score.



## 四.正则表达式（regular expression）



​	正则表达式，又称正规表示式、正规表示法、正规表达式、规则表达式、常规表示法（英语：Regular Expression，在代码中常简写为regex、regexp或RE），计算机科学的一个概念。正则表达式使用单个字符串来描述、匹配一系列匹配某个句法规则的字符串。在很多文本编辑器里，正则表达式通常被用来检索、替换那些匹配某个模式的文本。 许多程序设计语言都支持利用正则表达式进行字符串操作。例如，在Perl中就内建了一个功能强大的正则表达式引擎。正则表达式这个概念最初是由Unix中的工具软件（例如sed和grep）普及开的。正则表达式通常缩写成“regex”，单数有regexp、regex，复数有regexps、regexes、regexen。 

### 1.小甜点

有时间我们遇到一个如何查看一个字符串是否包含另外一个字符串的时候一般使用的是indexof或者in都可以解决。

例如：

```python
a = 'demo|node|captcha|goods'
# 传统方法判断一个字符串在一个字符串中
# if(a.index('node')>-1):
#     print("exist")
# else:
#     print("not exist")

if('node1' in a):
    print('exist')
else:
    print("not exist")
```

那除了这个方法我们还可以使用python的re模块来使用正则完成相关操作。

```python
# 使用re 模块来匹配
import re
a = 'demo|node|captcha|goods'
rest =re.findall('node',a)
# 这里获取的是一个list的数据类型
# print(type(rest))
# 扩展我们如何转成string类型呢
str = (''.join(rest))
print(type(str))
```

使用re模块我们很容易的就完成了一个简单的正则匹配。是不是很简单呢。^_____^

### 2.普通字符与元字符

```python
import re
str = '0as0xq12javaPHPhelloimg'

# \d	匹配一个数字字符。等价于 [0-9]。
# \D	匹配一个非数字字符。等价于 [^0-9]。
# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。

rest = re.findall('\d',str)
for i in rest:
    print((''.join(i)))
print(rest)

```










