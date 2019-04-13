
## Python3 内置函数学习

![](https://raw.githubusercontent.com/Hatcat123/GraphicBed/master/Img/20190413200306.png)


## 目录：

- [0x01abs](#0x01abs)
- [0x02divmod](#0x02divmod)
- [0x07enumerate](#0x07enumerate)
- [0x12eval](#0x12eval)
- [0x17execfile](#0x17execfile)
- [0x22file](#0x22file)
- [0x27filter](#0x27filter)
- [0x32float](#0x32float)
- [0x37format](#0x37format)


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