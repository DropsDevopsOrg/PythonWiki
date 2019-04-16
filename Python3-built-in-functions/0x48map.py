#map() 会根据提供的函数对指定序列做映射。第一个参数是函数，第二个参数是序列
#把序列里面的每个元素作为参数传递到函数，返回一个迭代器

def square(x):
    return x**2
ls = [1, 2, 3]

for i in map(square, ls):
    print(i)