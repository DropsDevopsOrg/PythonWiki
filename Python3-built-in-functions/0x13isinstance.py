#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
#另外isinstance判断对象是否为某一类型,返回true或false

a = 3
print(type(a))
str0 = "liang"
print(type(str0))

print(isinstance(a, int))
print(isinstance(a, str))
print(isinstance(str0, str))