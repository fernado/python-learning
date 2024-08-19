"""

zip: 可以把多个可迭代内容进行合并

sorted: 排序
"""

lst = [11, 22, 66, 1, 222, 39, 14]
# [1, 11, 14, 22, 39, 66, 222]
ss = sorted(lst)
print(ss)

# [222, 66, 39, 22, 14, 11, 1]
ss = sorted(lst, reverse=True)
print(ss)

#        2       3       2       5
lst = ["绿巨人", "牛夫人", "雷神", "超级赛亚人"]
ss = sorted(lst, key=str.lower)
print(ss)


def sort_a(item):
    return len(item)


# 排序长度
ss = sorted(lst, key=sort_a)
print(ss)

fn_sort = lambda x: len(x)
ss = sorted(lst, key=fn_sort)
print(ss)

ss = sorted(lst, key=lambda x: len(x))
print(ss)

lst = [
    {"id": 1, "name": "Jack", "age": 19, "salary": 12000},
    {"id": 2, "name": "Allen", "age": 12, "salary": 4500},
    {"id": 3, "name": "James", "age": 16, "salary": 3000},
    {"id": 4, "name": "Flora", "age": 29, "salary": 5000},
    {"id": 5, "name": "Lad", "age": 15, "salary": 9000},
]

# 根据年龄升序排序
ss = sorted(lst, key=lambda a: a["age"])
print(ss)

# 根据工资降序排序
ss = sorted(lst, key=lambda a: a["salary"], reverse=True)
print(ss)