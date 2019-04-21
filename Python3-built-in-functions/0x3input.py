#input()接受输入数据，返回类型为string
#后面加上.split()方法可接受多个数据输入

a = input("请输入：")

print(a, type(a))

a,b = input("请输入至少两个数据：").split()#多个数据输入
print(a, b)

name, age, QQ = input("请输入姓名，年龄，QQ号码:").split()

print("姓名：%s, 年龄：%s, QQ号码：%s" %(name, age, QQ))