class Test():
        color = 'white'


a1 = Test()
print(getattr(a1, 'color'))

a2 = Test()
print(getattr(a2, 'say', 'chinese'))

a3 = Test()
print(getattr(a3, 'other'))
