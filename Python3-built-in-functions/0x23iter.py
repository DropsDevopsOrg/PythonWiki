#iter()用来生成迭代器，参数为支持可迭代的对象
#列表 元组 字典 字符串是可迭代的，但不是迭代器
#迭代器被next()函数调用，不断返回下一个值

#字符串
s = 'qerty'
for i in iter(s):
    print(i)
#列表
l = [1, 2, 3, 4]
for i in iter(l):
    print(i,end='\t')
print('\n')
#元祖
m = (1, 2, 3, 4)
for i in iter(m):
    print(i,end='\t')
print('\n')
#字典
n = {'id': 1, "name": "liang", "user": "admin", "passworld": "123456"}
for i in iter(n):       #默认打印键名
    print(i)
for i in iter(n.values()):  #打印值
    print(i)