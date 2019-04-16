
## Python3 内置函数学习

![](https://raw.githubusercontent.com/Hatcat123/GraphicBed/master/Img/20190413200306.png)


## 目录：

- [0x01abs](#0x01abs)
- [0x02divmod](#0x02divmod)
- [0x03input](#0x03input)
- [0x07enumerate](#0x07enumerate)
- [0x08int](#0x08int)
- [0x12eval](#0x12eval)
- [0x13isinstance](#0x13isinstance)
- [0x17execfile](#0x17execfile)
- [0x18issubclass](#0x18issubclass)
- [0x22file](#0x22file)
- [0x23iter](#0x23iter)
- [0x27filter](#0x27filter)
- [0x28len](#0x28len)
- [0x32float](#0x32float)
- [0x33list](#0x33list)
- [0x37format](#0x37format)
- [0x38locals](#0x38locals)
- [0x42frozenset](#0x42frozenset)
- [0x43long](#0x43long)
- [0x47getattr](#0x47getattr)
- [0x48map](#0x48map)
- [0x52globals](#0x52globals)
- [0x53max](#0x53max)
- [0x57hasattr](#0x57hasattr)
- [0x58memoryview](#0x58memoryview)
- [0x62hash](#0x62hash)
- [0x63min](#0x63min)
- [0x67help](#0x67help)
- [0x68next](#0x68next)
- [0x72hex](#0x72hex)
- [0x73object](#0x73object)
- [0x77id](#0x77id)
- [0x78oct](#0x78oct)


# [0x01abs](0x01abs.py)

abs():求绝对值

```
print('正数浮点型： abs(12.50): ', abs(12.50))
print('负整数： abs(-12): ', abs(-12))
print('负数浮点型： abs(-12.4): ', abs(-12.4))
print('abs(2e5): ', abs(2e5))

# 可以用complex函数构造复数，complex(a, b)为a+bj
complex_exm = complex(1, 2)
# 复数格式化用%s或%r均可
print('复数： abs(%s): ' % complex_exm, abs(complex_exm))


# 输出结果：
'''
正数浮点型： abs(12.50):  12.5
负整数： abs(-12):  12
负数浮点型： abs(-12.4):  12.4
abs(2e5):  200000.0
复数： abs((1+2j)):  2.23606797749979
'''
```


# [0x02divmod](0x15divmod.py)
divmod(a, b):返回一个元组，包含a除以b的商及余数

``` python
print(divmod(7,2))

print(divmod(10,5))

# 输出结果：
'''
(3, 1)
(2, 0)
'''
```

# [0x03input](0x03input.py)

input()：接受输入数据，返回类型为string，后面加上.split()方法可接受多个数据输入

```

a = input("请输入：")

print(a, type(a))

a,b = input("请输入至少两个数据：").split()#多个数据输入

print(a, b)

name, age, QQ = input("请输入姓名，年龄，QQ号码:").split()

print("姓名：%s, 年龄：%s, QQ号码：%s" %(name, age, QQ))

#输出结果
请输入：1

<class 'str'> 1

请输入至少两个数据：1 2

1 2

请输入姓名，年龄，QQ号码:2 12 45648

姓名：2, 年龄：12, QQ号码：45648


```

# [0x07enumerate](0x16enumerate.py)
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

``` python
a = 'hello'

print(enumerate(a))

for i in enumerate(a):
        print(i)

for i, j in enumerate(a):
        print(i, j)

# 输出结果：
'''
<enumerate object at 0x03527508>
(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
0 h
1 e
2 l
3 l
4 o
'''
```
# [0x08int](0x08int.py)

int() 函数用于将一个字符串或数字转换为整型,后面可跟进制类型

```

print(int())    #空转换成为

print(int(3.6)) #转换浮点型，不会四舍五入

print(int('123465'))    #转换字符串

print(int('110', 2))    #把2进制的110转换成十进制

print(int("12", 8))     #把8进制的12转换成十进制

print(int("12", 16))    #把16进制的12转换成十进制


#输出结果
0
3
123465
6
10
18

```

# [0x12eval](0x17eval.py)
将字符串str当成有效的表达式来求值并返回计算结果

``` python
a = '((2 + 3*2)/2)'
print(eval(a))

b = 'input("please input a number: ")'
print(eval(b))

test1 = "['a','b','c','d']"
print(eval(test1))
print(type(eval(test1)))

test2 = "{'a':'b'}"
print(eval(test2))
print(type(eval(test2)))

# 输出结果：
'''
4.0
please input a number: 5
5
['a', 'b', 'c', 'd']
<class 'list'>
{'a': 'b'}
<class 'dict'>
'''
```

这个函数也缺少安全性：

如，想根据用户输入表达式来求值

``` python
safe = input('please input a expression: ')
print(eval(safe))
```

结果用户输入： `open('0x15divmod.py').read()`，则会输出这个文件中的内容，那么用户即可访问自己的所有文件；不仅是访问文件，还可进行其他操作

# [0x13isinstance](0x13isinstance.py)
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type(),另外isinstance判断对象是否为某一类型,返回true或false

```
a = 3

print(type(a))

str0 = "liang"

print(type(str0))

print(isinstance(a, int))

print(isinstance(a, str))

print(isinstance(str0, str))

#输出结果
<class 'int'>

<class 'str'>

True

False

True
```

# [0x17execfile](#0x17execfile.py)

python3取消了execfile()函数

exec():执行string类型变量存储的代码，并不输出结果

``` python
a = '(2+(2*4))/5'
print(exec(a))
print(eval(a))
print('='*10)
b = 'exp=(2+(2*4))/5'
exec(b)
print(exp)
print(eval(b))

# 输出结果：
'''
None
2.0
==========
2.0
Traceback (most recent call last):
  File "C:\Users\腾飞\Desktop\研发\python3内置函数\0x18exec.py", line 8, in <module>
    print(eval(b))
  File "<string>", line 1
    exp=(2+(2*4))/5
       ^
SyntaxError: invalid syntax
'''
```

# [0x18issubclass](#0x18issubclass.py)
issubclass(A,B) 方法用于判断参数A是否是类型参数B的子类,是则返回true，否则返回false
```
class A:
    pass
class B(A):
    pass
class C:
    pass
print(issubclass(B, A))  # 返回 True
print(issubclass(C, A))  #返回false

#运行结果
"""
True
False

"""
```


# [0x22file](#0x22file.py)

file()可以创建一个file对象，同open()作用相同

python3不支持file()函数了

``` python
f = open('0x22test.txt', 'r')
print(f.readlines())

# 输出结果：
'''
['hello\n', 'world']
'''
```

# [0x23iter](#0x23iter.py)
iter()用来生成迭代器，参数为支持可迭代的对象

```
字符串
s = 'qerty'
for i in iter(s):
    print(i)
列表
l = [1, 2, 3, 4]
for i in iter(l):
    print(i,end='\t')
print('\n')
元祖
m = (1, 2, 3, 4)
for i in iter(m):
    print(i,end='\t')
print('\n')
字典
n = {'id': 1, "name": "liang", "user": "admin", "passworld": "123456"}
for i in iter(n):       #默认打印键名
    print(i)
for i in iter(n.values()):  #打印值
    print(i)
    
#运行结果
"""
q
e
r
t
y
1	2	3	4	
1	2	3	4	
id
name
user
passworld
1
liang
admin
123456
"""
```
# [0x27filter](#0x27filter.py)

filter()函数用于过滤序列，返回一个迭代对象，可用list()转换为序列

语法：`filter(function, iterable)`

``` python
def func(num):
        if num < 5:
                return 1
        

a = [x for x in range(10)]

print(filter(func, a))
print(list(filter(func, a)))

# 输出结果：
'''
<filter object at 0x03685110>
[0, 1, 2, 3, 4]
'''
```

# [0x28len](#0x28len.py)
len() 方法返回对象（字符、列表、元组等）长度
```
数组类型
print(len([1, 2, 3, 4, 5, 6]))
元祖类型
print(len((1, 2, 3, 4, 5, )))
字典类型
print(len({'id': 1, "user": "admin", "password": "123465"}))
字符串类型
print(len('efarg  gg g'))

#运行结果
"""
6
5
3
11
"""
```

# [0x32float](#0x32float.py)

将整数和字符串转换为浮点数

``` python
print(float(0))
print(float(1))
print(float(-1))
print(float(1.002))
print(float(1.0000))
print(float('1.3'))

# 输出结果：
'''
0.0
1.0
-1.0
1.002
1.0
1.3
'''
```

# [0x33list](#0x33list.py)
list()将元组或字符串转换成列表
```
a = (1,2,3)
print(a)
print(list(a))
b = "liangweiyang"
print(b)
print(list(b))

#运行结果
"""
(1, 2, 3)
[1, 2, 3]
liangweiyang
['l', 'i', 'a', 'n', 'g', 'w', 'e', 'i', 'y', 'a', 'n', 'g']
"""
```

# [0x37format](#0x37format.py)

格式化字符串，功能多于 `%`

``` python 
print("{}{}".format('hello', 'world'))
# 不指定位置，默认从左往右

print("{1}{0}".format('hello', 'world'))
# 在大括号中指定顺序

print("{user} {pawd}".format(user='admin', pawd='password'))
# 指定参数

# 输出结果：
'''
helloworld
worldhello
admin password
'''
```

# [0x38locals](#0x38locals.py)
locals() 函数会以字典类型返回当前位置的全部局部变量,不需要参数,变量为为键，变量的值为键的值
```
def func(): #在函数内部定义两个局部变量
    s = 1
    y = 2
    print(locals())

func()      #调用自定义方法

#运行结果
{'s': 1, 'y': 2}
```

# [0x42frozenset](#0x42frozenset.py)

将可迭代对象设置成冻结的集合；无参数会返回空集合

``` python
a = [1, 2, 3]
b = frozenset(a)
print(b)
print(frozenset())

# 输出结果：
'''
frozenset({1, 2, 3})
frozenset()
'''
```

# [0x43long](#0x43long.py)
long() 函数将数字或字符串转换为一个长整型
```
a = 123
print(type(a))
print(type(long(a)))

s = '456'
print(type(s))
print(type(long(b)))
```

# [0x47getattr](#0x47getattr.py)

返回一个对象的属性值

```
class Test():
        color = 'white'


a1 = Test()
print(getattr(a1, 'color')) 
# 如果属性名存在则返回其值

a2 = Test()
print(getattr(a2, 'say', 'chinese')) 
# 如果属性名不存在则返回设定的返回值

a3 = Test()
print(getattr(a3, 'other')) 
# 属性名不存在且没有设定返回值则会报错

# 输出结果：
'''
white
chinese
Traceback (most recent call last):
  File "C:\Users\腾飞\Desktop\研发\PythonWiki\Python3-built-in-functions\0x47getattr.py", line 12, in <module>
    print(getattr(a3, 'other'))
AttributeError: 'Test' object has no attribute 'other'
'''
```

# [0x48map.py](#0x48map.py)
会根据提供的函数对指定序列做映射。第一个参数是函数，第二个参数是序列
```
def square(x):
    return x**2
ls = [1, 2, 3]

for i in map(square, ls):
    print(i)

#运行结果
"""
1
4
9
"""
```

# [0x52globals](#0x52globals.py)

globals()函数以字典形式返回当前位置的所有全局变量

``` python
a = 'hello'
b = 'world'

print(globals())

# 输出结果：
'''
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\腾飞\\Desktop\\研发\\PythonWiki\\Python3-built-in-functions\\0x52globals.py', 'a': 'hello', 'b': 'world'}
'''
```

# [0x53max](#0x53max.py)
max() 方法返回给定参数的最大值，可比较字符.汉字和表达式
```
print(max(1, 2, 3, 45, 4))
print(max([1, 2, 3, 4, 5, 6]))
print(max('a', 'b', 'c', 'd'))
print(max('梁', '伟', '洋'))
print(max(8+2, 1+1, 9+9))

#运行结果
"""
45
6
d
洋
18
"""
```

# [0x57hasattr](#0x57hasattr.py)

判断对象是否包含某个属性，如果包含返回True，否则返回False

``` python
class Test():
        color = 'white'


a1 = Test()
print(hasattr(a1, 'color'))

print(hasattr(a1, 'say'))

# 输出结果：
'''
True
False
'''
```

# [0x58memoryview](#0x58memoryview.py)
memoryview() 函数返回给定参数的内存查看对象，这个找了一下资料，自己也没看太懂
```
v = memoryview(bytearray("abcefg", 'utf-8'))
print(type(v))
print(v[1])

#运行结果
"""
<class 'memoryview'>
98
"""
```

# [0x62hash](#0x62hash.py)

返回一个对象的哈希值；对象可以是整型、字符串，但不能直接用于列表、字典等

具有相同值的对象具有相同的hash值；对象的hash值不仅与对象的内容有关，还与对象的内存地址有关

``` python
a = 1
b = 1.0
print(hash(a))
print(hash(b))

c = 'hello'
d = 'world'
print(hash(c))
print(hash(d))
print(hash('今天是个好日子'))
# 输出结果：
'''
1
1
1604966843
1326011668
-1235082111
'''
```

# [0x63min](#0x63min.py)
min()方法返回给定参数的最小值，可比较字符.汉字和表达式
```
print(min(1, 2, 3, 45, 4))
print(min([1, 2, 3, 4, 5, 6]))
print(min('a', 'b', 'c', 'd'))
print(min('梁', '伟', '洋'))
print(min(8+2, 1+1, 9+9))

#运行结果
"""
1
1
a
伟
2
"""
```

# [0x67help](#0x67help.py)

返回函数或模块的详细说明

``` python
print(help('str'))

# 输出结果太多，省略...
```

# [0x68next](#0x68next.py)
next()返回迭代器的下一项
```
l = [1, 2, 3, 4]
li = iter(l)
for i in l:
    y = next(li)
    print(y)
    
#运行结果
"""
1
2
3
4
"""
```


# [0x72hex](#0x72hex.py)

将整型数字转换为其对应的16进制，结果并不是固定长度

``` python
print(hex(1))
print(hex(10))
print(hex(100))
print(hex(257))

print(hex(1.0))

# 输出结果：
'''
0x1
0xa
0x64
0x101
Traceback (most recent call last):
  File "C:\Users\腾飞\Desktop\研发\PythonWiki\Python3-built-in-functions\0x72hex.py", line 4, in <module>
    print(hex(1.0))
TypeError: 'float' object cannot be interpreted as an integer
'''
```

# [0x73object](#0x73object.py)
Object类是Python中所有类的基类，如果定义一个类时没有指定继承那个类，则默认继承object类
```
class A:
    pass
class B(A):
    pass
print(issubclass(A, object))
print(issubclass(B, A))
print(issubclass(B, object))

#运行结果
"""
True
True
True
"""
```


# [0x77id](#0x77id.py)

获取对象的内存地址

Cpython(用C语言写的python)在编译优化时，会尝试使用已经存在的不可变对象而不是每次都创建一个新对象

``` python
a = 'some_string'
b = 'some' + '_' + 'string'
c = 'somestring'

print(id(a))
print(id(b))
print(id(c))

# 输出结果：
'''
56522176
56522176
56522776
'''
```

# [0x78oct](#0x78oct.py)
oct() 函数将一个整数转换成8进制字符串,返回字符串类型
```
print(oct(16))
print(type(oct(10)))

#运行结果
"""
0o20
<class 'str'>
"""
```
