#issubclass(A,B) 方法用于判断参数A是否是类型参数B的子类
#是则返回true，否则返回false
class A:
    pass
class B(A):
    pass
class C:
    pass
print(issubclass(B, A))  # 返回 True
print(issubclass(C, A))  #返回false