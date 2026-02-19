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