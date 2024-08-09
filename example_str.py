from pydantic import BaseModel
import pandas as pd

class Student(BaseModel):
    name: str
    age: int


lst = [Student(name='fernando', age=30), Student(name='John', age=32)]

print(lst)

ss = "[Student(name='fernando', age=30), Student(name='John', age=32)]"

sts = eval(ss)

print(sts)


for st in sts:
    print(f"Name: {st.name}, Age: {st.age}")

data = [student.dict() for student in sts]

df = pd.DataFrame(data)

print(df)

for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['name']}, Age: {row['age']}")




