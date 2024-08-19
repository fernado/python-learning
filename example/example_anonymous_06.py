"""

zip: 可以把多个可迭代内容进行合并

sorted: 排序

filter: 筛选

map: 映射
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
result = [item ** 2 for item in lst]
print(result)


m = map(lambda x: x ** 2, lst)
# <map object at 0x018DEC28>
print(m)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list(m))

