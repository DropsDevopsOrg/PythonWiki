def func(num):
        if num < 5:
                return 1
        

a = [x for x in range(10)]

print(filter(func, a))
print(list(filter(func, a)))
