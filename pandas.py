import pandas as pd

# df = pd.read_csv('fitness_data.csv')
# Step 1️⃣: Basics

# print(df.head())
# print(df.to_string())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())
# pulse = df['Pulse']
# print(pulse)
# print(df.loc[[5,9]])
# print(df.iloc[0:4])
# print(df.loc[0:5,['Pulse','Calories']])
# print('mean pulse :', df['Pulse'].mean())
# print('median pulse :', df['Pulse'].median())
# print('mode pulse :', df['Pulse'].mode())
# print('sum:', df['Pulse'].sum())
# print('values count:',df['Pulse'].value_counts())
# print(df.loc[0:5, 'Pulse'])


# Step 2️⃣: Data Cleaning
# 🔹 Step 2.1 — Check Missing Values
# print(df.isna().sum())


# 🔹 Step 2.2 — Remove Rows and columns
# print(df.dropna(subset = ['Pulse']))# drop tarvata output
# df_clean = df.dropna(subset=['Pulse'])# here after drop tarvata  sum output
# print(df_clean.isna().sum())
# df.dropna(inplace = True)
# print(df.to_string())

# df.dropna(subset = ['Pulse'], inplace = True)# for row delete
# print(df.to_string())
# df.dropna(subset = ['Pulse', 'Calories'], inplace = True)
# print(df.to_string())

# df.drop(['Pulse'], axis=1, inplace=True)# for column delete
# print(df.to_string())

# Case 3 → Remove column Maxpulse, calories
# df.drop(['Maxpulse', 'Calories'], axis=1, inplace=True)
# print(df.to_string())

# Case 1 → Remove rows 3,5
# df.drop([3,5], axis=0, inplace=True)
# print(df.to_string())

# Case 3 → Remove column Maxpulse
# df.drop('Maxpulse', axis=1, inplace = True)
# print(df.to_string())

# Case 2 → Remove row 3
# df.drop(3, axis=0, inplace = True)
# print(df.to_string())


# 🔹 Step 2.3 — Fill Missing rows and columns
# ✅ Replace Empty Values:
# df = pd.read_csv('fitness_data.csv')
# df.fillna(130, inplace = True)
# print(df.to_string())# 130 filled with all Nan

# ✅ Replace Only For Specified or 1  Column
# df= pd.read_csv('fitness_data.csv')
# df.fillna({"Duration": 20}, inplace = True)
# print(df.to_string())# only for duration we filled


# ✅ Replace Using Mean, Median, or Mode
# df = pd.read_csv('fitness_data.csv')
# x = df["Calories"].mean()
# df.fillna({"Calories":x}, inplace = True)
# print(df.to_string())

# df = pd.read_csv('fitness_data.csv')
# x = df["Duration"].median()
# df.fillna({"Duration": x}, inplace=True)
# print(df.to_string())

# df = pd.read_csv('fitness_data.csv')
# x = df["Pulse"].mode()[0]
# df.fillna({"Pulse":x}, inplace = True)
# print(df.to_string())


# Step 2: Fill only 2 columns or 3 column
# df = pd.read_csv('fitness_data.csv')
# df[['Pulse', 'Calories','Duration']]= df[['Pulse', 'Calories','Duration']].fillna(130)
# print(df.to_string())

# 🔹 Step 2.4 — Convert Date to Proper Datetime
# df = pd.read_csv('fitness_data.csv')
# df['Date'] = pd.to_datetime(df['Date'], format = 'mixed')# fix correct format
# # df['Date'] = pd.to_datetime(df['Date'], errors='coerce')# covert wrong to Nan
# print(df.to_string())
# print(df.info())

# for other than date columns to check and changr format
# df = pd.read_csv('fitness_data.csv')
# df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')
# print(df.to_string())


# 🔹 Step 2.5 — Remove Duplicates

# duplicates = df[df.duplicated()]
# print(duplicates.to_string())# show duplicate rows
# df.drop_duplicates(inplace = True) # drop all duploicates
# print(df.to_string())

#You are adding a duplicate row with pd.concat: 1 row added at end 1 means index
# df = pd.concat([df, df.iloc[[0]]])
# df = df.drop_duplicates()# remove duplicates
# print(df.to_string())

#df = df.drop_duplicates(subset=["Name", "Age"]) by column names
#print(df.to_string())


#You are adding a duplicate row with pd.concat: 1 row added at end 1 means index
# df = pd.concat([df, df.iloc[[1]]])
# Drop duplicates and reset index
# df = df.drop_duplicates().reset_index(drop=True) # same as above
# print(df.to_string())


# change for multiple vlues:
# df = pd.read_csv('fitness_data.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120

# print(df.to_string())

#  another way delete rows:

# df = pd.read_csv('fitness_data.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)
# print(df.to_string())



# 4️⃣ Aggregation & Grouping
# df = pd.read_csv('fitness_data.csv')
# result = df.groupby('Duration')['Calories'].mean()
# print(result)
# ✅ Interpretation: example of mean :
# For Duration = 30, there are 2 rows: 200 & 180 → mean = 190
# For Duration = 45, mean = (250 + 220)/2 = 235
# For Duration = 60, only one row → 300

# result = df.groupby('Pulse')['Maxpulse'].max()#(max of pulses)
# print(result)


#2️⃣ Aggregate Multiple Functions:
# df = pd.read_csv('fitness_data.csv')
# result = df.groupby('Duration').agg({'Calories': 'mean', "Pulse":'max'})
# print(result)

#  same as above just pivot table :
# df.pivot_table(index='column_to_group', values='column_to_aggregate', aggfunc='function')
# result = df.pivot_table(index='Duration', values='Calories', aggfunc='mean')
# print(result)

#  multiple values agg:

# result = df.pivot_table(index='Duration', values=['Calories','Pulse'], aggfunc={'Calories':'mean','Pulse':'max'})
# print(result)

# 5️⃣ Sorting & Ranking
#a) Sort rows by a column
# df = pd.read_csv('fitness_data.csv')
# df_sorted = df.sort_values('Calories', ascending=False) # large to small
# print(df_sorted.to_string())
# df_sorted2 = df.sort_values('Calories', ascending=True) # small to large
# print(df_sorted2.to_string())

# df_index=df.sort_index()
# print(df_index.to_string())

# df_rank = df['Calories'].rank()
# print(df_rank.to_string())

# 6️⃣ Merging & Joining
# df1 = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Name": ["John", "Anna", "Mike"]})
# df2 = pd.DataFrame({
#     "ID": [4, 5],
#     "Name": ["Sara", "Tom"]})
#
# df_concat = pd.concat([df1, df2])# index duplicate
# print(df_concat)
# df_concat = df_concat.reset_index(drop=True)# index reset
# print(df_concat)
#
# # 2️⃣ Merge (SQL-style join)
# df1 = pd.DataFrame({
#     "ID": [1, 2, 3],
#     "Name": ["John", "Anna", "Mike"]})
# df2 = pd.DataFrame({
#     "ID": [2, 3, 4],
#     "Salary": [50000, 60000, 55000]})
#
# pd_merge = pd.merge(df1, df2, on= 'ID', how = 'inner')
# print(pd_merge)
#
# # Other how options:
# # how='left' → all rows from df1, fill missing with NaN
# # how='right' → all rows from df2
# # how='outer' → all rows from both, missing filled with NaN
#
# # 3️⃣ Join on index
# # Sample data
# df1 = pd.DataFrame({
#     "Name": ["John", "Anna", "Mike"]})
# df2 = pd.DataFrame({
#     "Salary": [50000, 60000, 55000]})
# # Join using index
# df_join = df1.join(df2)
# print(df_join)


# 7️⃣ Reshaping
# a) Melt / unpivot
# import pandas as pd
# df = pd.DataFrame({
#     "Duration": [30, 45, 30, 45],
#     "Pulse": [110, 120, 115, 125],
#     "Calories": [200, 250, 180, 220]})
# print(df)#original

# 1️⃣ Melt (long format)
# We want one column for variable,one for value, keeping Duration fixed:
# df_melted = pd.melt(df, id_vars='Duration', value_vars=['Pulse','Calories'])
# print(df_melted)

# 2️⃣ Pivot (wide format)
# Suppose now we want Duration as rows and Pulse as columns, with Calories as values:
# df_pivot = df.pivot(index='Duration', columns='Pulse', values='Calories')
# print(df_pivot)

# 3️⃣ Bonus: Pivot Table with aggregation
# If there are multiple Calories per Duration & Pulse, we can aggregate:
# df_pivot_table = df.pivot_table(index='Duration', columns='Pulse', values='Calories', aggfunc='mean')
# print(df_pivot_table)

# 8️⃣ Applying Functions
import pandas as pd

df = pd.DataFrame({
    "Calories": [200, 250, 180, 220]})
df['Calories'] = df['Calories'].apply(lambda x: x/10)
print(df)

# b) Vectorized operations (fast & simple)
df['Calories'] = df['Calories'] +50
print(df)

# c) Map / Replace values
df = pd.DataFrame({
    "Pulse": [100, 110, 120]
})
df['Pulse'] = df['Pulse'].map({100:'low', 110:'medium', 120:'high'})
print(df)

# 9️⃣ Statistics & Correlation

df = pd.DataFrame({
    "Duration": [30, 45, 30, 45],
    "Pulse": [110, 120, 115, 125],
    "Calories": [200, 250, 180, 220]
})
print(df.corr())
print(df.cov())
print(df.describe())





import csv
import pandas as pd
import numpy as np

df = pd.read_csv('mini_project.csv')
print(df.to_string())

df['Quantity']= pd.to_numeric(df['Quantity'], errors = 'coerce')
df['Price'] = pd.to_numeric(df['Price'], errors = 'coerce')
df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors = 'coerce')

# df = df.dropna() in this way many rows get del bcoz all nan  rows removed
df.dropna(subset = ['Quantity', 'Price'], inplace = True)
df['Revenue'] = df['Quantity'] * df['Price']

print(df.groupby('Product')['Revenue'].sum().sort_values(ascending=False))# big to small
# print(df.groupby('Product')['Revenue'].sum().sort_values(ascending=True))# small to big
print(df.groupby('Product')['OrderDate'].min())

df.to_csv("retail_sales_cleaned.csv", index=False)

with open('retail_sales_cleaned.csv', 'r', newline='')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)