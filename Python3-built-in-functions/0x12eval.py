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


safe = input('please input a expression: ')
print(eval(safe))
