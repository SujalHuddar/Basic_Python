import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Kiran", "Rohit", "Anjali", "Vikas"],
    "Department": ["CSE", "ECE", "CSE", "ISE", "ECE", "CSE", "ISE", "ECE"],
    "Marks": [78, 65, 92, 55, 88, 72, 95, 61],
    "City": ["Belgaum", "Hubli", "Belgaum", "Bangalore",
             "Hubli", "Belgaum", "Bangalore", "Hubli"]
}

df = pd.DataFrame(data)

print(df)

# 1. Find all students who scored more than 75.
more_75 = df[df['Marks']>75]
print(more_75)

# 2. Find all CSE students.
cse = df[df['Department'] == 'CSE']
print(cse)

# 3. Find the average marks of each department using groupby().
avg = df.groupby('Department')['Marks'].mean()
print(avg)

# 4. Find the highest marks in each department.
highest_marks = df.groupby('Department')['Marks'].max()
print(highest_marks)

#5. Find how many students are from each city.
city = df.groupby('City').size()
print(city)
                 #or#
                 # df['City].value_counts()

#6. Find the student who has the highest marks among CSE students.
highest_cse = df[df['Department'] == 'CSE'].loc[df[df['Department'] == 'CSE']['Marks'].idxmax()]
print(highest_cse)

#7. Find the department with the highest average marks.
avg_marks = df.groupby('Department')['Marks'].mean()
highest_dep = avg_marks.idxmax()
print(highest_dep)