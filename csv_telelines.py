import csv

with open('tele.csv', 'w', newline = "")as file:
    writer = csv.writer(file)
    writer.writerow(['names', 'cost', 'quantity'])
    writer.writerow(['airtel', 10,5])
    writer.writerow(['jio', 5, 10])
    writer.writerow(['idea', 2, 20])

print('tele.csv file created')


# ✅ 1️⃣ Writing Multiple Rows Using a List (csv.writer)

# data = (['names', 'price', 'quantity'],['airtel', 10,5],['jio', 5, 10],['idea', 2, 20])
#
# with open('tele.csv', 'w', newline = '')as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print('file written 2nd way')

# ✅ 2️⃣ Writing Multiple Rows Using Loop (Alternative Way)

# data = (['names', 'price', 'quantity'],['airtel', 10,5],['jio', 5, 10],['idea', 2, 20])

# with open("tele.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#
#     for row in data:
#         writer.writerow(row)
# print('tele.csv created 3rd way by loop')


# ✅ 3️⃣ Using DictWriter with Multiple Rows

# data = [
#     {"Product": "Laptop", "Quantity": 5, "Price": 1000},
#     {"Product": "Phone", "Quantity": 10, "Price": 500},
#     {"Product": "Tablet", "Quantity": 7, "Price": 300}
# ]
#
# fieldnames = ['Product', 'Price', 'Quantity']
#
# with open("tele.csv", "w", newline="") as file:
#     writer=csv.DictWriter(file,fieldnames = fieldnames)
#     writer.writeheader()
#     writer.writerows(data)
#
#
# print('dict written data')

# 🔹 2️⃣ Regular Read → csv.reader()

# with open('tele.csv', mode = 'r', newline = "")as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#
# print('csv tele read successfully')

# 🔹 3️⃣ Dictionary Read → csv.DictReader()

with open('tele.csv', mode = 'r', newline = "")as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

print('csv tele read successfully')


# 🔹 3️⃣ Dictionary Read → csv.DictReader()

# with open("tele.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         names = row["names"]
#         quantity = int(row["quantity"])
#         cost = int(row["cost"])
#         print(names, quantity * cost)


# 🔹 2️⃣ Regular Read → csv.reader()

# with open("tele.csv", "r", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     next(reader)  # skip header
#     for row in reader:
#         names = row[0]
#         quantity = int(row[1])
#         cost = int(row[2])
#         print(names, quantity * cost)


# ✅ 3️⃣ Step 3: Append New Rows:

with open ('tele.csv', 'a', newline = "")as file:
    writer = csv.writer(file)
    writer.writerow(["vodaphone", 10,2])
    writer.writerow(["Bsnl",2,20])

print('new rows appended')

# # ✅ 3️⃣ Step 3: Append New Rows as 2nd way:
#
# data = [["vodaphone", 10,2],["Bsnl", 2,200]]
# with open ('tele.csv', 'a', newline = "")as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#
# print('2nd way append')


# ✅ 2️⃣ Append Using csv.DictWriter:
# data = [{'names':'vodaphone','cost':2, 'quantity':20},
#     {'names': 'Bsnl', 'cost': 2, 'quantity': 20}]
#
# fieldnames = ['names', 'cost','quantity']
# with open ('tele.csv', mode = 'a', newline = '')as file:
#     writer = csv.DictWriter(file, fieldnames= fieldnames)
#     # ❌ DO NOT write header again when appending, bcoz alredy there in write header, so no need again
#     writer.writerows(data)

# print('data appended successfully in dict way')

# 🔹 3️⃣ Append Single Row (One Dictionary)

# new_row = {"names": "verizon", "quantity": 15, "cost": 20}
#
# with open("tele.csv", "a", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=["names", "quantity", "cost"])
#     writer.writerow(new_row)
#
# print('ony one line addaed through dict')



updated_rows = []

# Step 1: Read and update in memory
with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    for row in reader:
        row['revenue'] = int(row['quantity']) * int(row['cost'])
        updated_rows.append(row)

# Step 2: Add new column to fieldnames
fieldnames.append('revenue')

# Step 3: Write updated rows back to file
with open('tele.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

# Step 4: Read again to verify
with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
print('added column')

# 🔹 Case 1: Delete all rows that have any empty cell
updated_rows = []

# Step 1: Read CSV
with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames

    for row in reader:
        # Update price if quantity > 5
        if int(row['quantity']) > 5:
            row['cost'] = int(row['cost']) * 1.1  # increase 10%

        # Update revenue column
        row['revenue'] = int(row['quantity']) * int(row['cost'])
        updated_rows.append(row)

# Step 2: Write updated CSV
with open('tele.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

# Step 4: Read again to verify

with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
print('added column')

print("CSV updated with new prices and revenue!")

# 🔹 1️⃣ Filter Rows by Condition

filtered_rows = []

with open('tele.csv', 'r', newline = '')as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    for row in reader:
        if int(row['quantity']) >5:
            filtered_rows.append(row)

for row in filtered_rows:
    print(row)

with open('tele.csv', 'w', newline = '')as file:
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerows(filtered_rows)


with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

print('filtered rows saved to filtered_tele.csv')


rows = []

# Step 1: Read CSV
with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    for row in reader:
        row['revenue'] = float(row['revenue'])  # make sure it’s numeric
        rows.append(row)

# Step 2: Sort rows by revenue ascending
rows_sorted_asc = sorted(rows, key=lambda x: x['revenue'])

# Step 3: Write to new file
with open('tele_sorted_asc.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_sorted_asc)

with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


print("CSV sorted ascending by revenue!")



updated_rows = []

with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames

    for row in reader:
        # Keep only rows where **all columns have data**
        if all(cell.strip() for cell in row.values()):
            updated_rows.append(row)

# Write back to a new CSV
with open('tele_clean_all_empty.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)

with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


print("Deleted all rows with any empty cell")


# 🔹 Case 2: Delete only rows where names = "vodaphone" (even if it has empty columns)

updated_rows = []

with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames

    for row in reader:
        # Keep row unless names = vodaphone
        if row['names'].strip().lower() != 'vodaphone':
            updated_rows.append(row)

# Write back to new CSV
with open('tele.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_rows)


with open('tele.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

print("Deleted only vodaphone row")




