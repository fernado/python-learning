from pydantic import BaseModel
import pandas as pd

class Student(BaseModel):
    name: str
    age: int


lst = [Student(name='fernando', age=30), Student(name='John', age=32)]

# [Student(name='fernando', age=30), Student(name='John', age=32)]
print(lst)

ss = "[Student(name='fernando', age=30), Student(name='John', age=32)]"

sts = eval(ss)
# [Student(name='fernando', age=30), Student(name='John', age=32)]
print(sts)

# Name: fernando, Age: 30
# Name: John, Age: 32
for st in sts:
    print(f"Name: {st.name}, Age: {st.age}")

data = [student.dict() for student in sts]

df = pd.DataFrame(data)

#        name  age
# 0  fernando   30
# 1      John   32
print(df)

# Index: 0, Name: fernando, Age: 30
# Index: 1, Name: John, Age: 32
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['name']}, Age: {row['age']}")




