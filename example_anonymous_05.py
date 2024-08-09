"""

zip: 可以把多个可迭代内容进行合并

sorted: 排序

filter: 筛选
"""

lst = ["张三", "张恒", "雷人", "雷神"]
f = filter(lambda x: x.startswith("雷"), lst)
# <filter object at 0x01E16CB8>
print(f)
print(list(f))

f = filter(lambda x: not x.startswith("雷"), lst)
# <filter object at 0x01E16CB8>
print(f)
print(list(f))


