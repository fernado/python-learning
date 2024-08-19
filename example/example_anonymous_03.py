"""

zip: 可以把多个可迭代内容进行合并

"""

#        0        1       2
lst1 = ["赵本山", "范伟", "苏有朋"]
lst2 = [40, 38, 42]
lst3 = ["卖拐", "耳朵大有福", "情深深雨濛濛"]


result = []
for i in range(0, len(lst1)):
    first = lst1[i]
    second = lst2[i]
    third = lst3[i]
    result.append([first, second, third])

print(result)


result = zip(lst1, lst2, lst3)
#<zip object at 0x010FF528>
print(result)
print(dir(result))

for item in result:
    print(item)


result = zip(lst1, lst2, lst3)
lst = list(result)
print(lst)


a = 111
# 此时locals 在此是属于全局作用域范围内，此时可以看到全局作用域的内容
print("locals-----------------1")
print(locals())
print("globals-----------------2")
print(globals())

def locals_func():
    a = 114
    print("locals-----------------3")
    print(locals())
    print("globals-----------------4")
    print(globals())


locals_func()
