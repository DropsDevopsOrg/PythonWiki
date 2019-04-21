#memoryview() 函数返回给定参数的内存查看对象，这个找了一下资料，自己也没看太懂

v = memoryview(bytearray("abcefg", 'utf-8'))
print(type(v))
print(v[1])