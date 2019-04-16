#next()返回迭代器的下一项

l = [1, 2, 3, 4]
li = iter(l)
for i in l:
    y = next(li)
    print(y)