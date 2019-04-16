#Object类是Python中所有类的基类，如果定义一个类时没有指定继承那个类，则默认继承object类

class A:
    pass
class B(A):
    pass
print(issubclass(A, object))
print(issubclass(B, A))
print(issubclass(B, object))