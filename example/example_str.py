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

# Index: 0, Name: fernando, Age: 30
# Index: 1, Name: John, Age: 32
# Iterate over each row as namedtuples
for row in df.itertuples(index=True, name='Student'):
    print(f"Index: {row.Index}, Name: {row.name}, Age: {row.age}")



# Column: name
# 0    fernando
# 1        John
# Name: name, dtype: object
# Column: age
# 0    30
# 1    32
# Name: age, dtype: int64

# Iterate over each column
for column in df:
    print(f"Column: {column}")
    print(df[column])



# fernando
# John
# 30
# 32

# Example function to print each cell
def print_cell(x):
    print(x)

# Apply the function to each cell
df.map(print_cell)



# Row 0, Column name: fernando
# Row 0, Column age: 30
# Row 1, Column name: John
# Row 1, Column age: 32

# Iterate over each row and each column within the row
for i in range(len(df)):
    for j in df.columns:
        print(f"Row {i}, Column {j}: {df.iloc[i][j]}")


# iterrows(): Iterate over rows as (index, Series) pairs.
# itertuples(): Iterate over rows as namedtuples, which is faster.
# Column iteration: Iterate over columns by looping through df.columns.
# map(): Apply a function to each cell in the DataFrame.
# Nested loops: Manually loop through each row and each column for cell-by-cell access.