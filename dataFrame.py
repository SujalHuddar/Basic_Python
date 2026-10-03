import pandas as pd

data = {
    "Name": ['Aditya','Praveen','Shashidhar','Shreyas','Satish'],
    "Age": [10,20,30,40,50],
    "Marks": [25,65,90,30,82]
}

df = pd.DataFrame(data)
print(data)

# Find the average marks
avg_m = df['Marks'].mean()
print("Average marks :",avg_m)

# Find students with higest marks
high = df.loc[df["Marks"].idxmax()]
print(high)

# Find students with lowest marks
low = df.loc[df["Marks"].idxmin()]
print(low)

#Find student who scored more then 70
more_70 = df[df['Marks'] > 70]
print(more_70)

#Sort student from higest to lowest
high_low = df.sort_values('Marks', ascending=False)
print(high_low)
