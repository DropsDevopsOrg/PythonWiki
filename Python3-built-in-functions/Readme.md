
## Python3 内置函数学习

![](https://raw.githubusercontent.com/Hatcat123/GraphicBed/master/Img/20190413200306.png)


## 目录：

- [0x01abs](#0x01abs)






### [0x01abs](0x01abs.py)

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