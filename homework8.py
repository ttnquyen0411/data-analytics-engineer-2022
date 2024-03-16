import csv


with open('dept_manager.csv') as csvfile:
    data = csv.DictReader(csvfile)

    for row in data:
        if row['dept_no'] == "d008" and row['to_date'] == "9999-01-01":
            key = row['emp_no']

with open('salaries.csv') as csvfile:
    data = csv.DictReader(csvfile)

    for row in data:
        if row['emp_no'] == key:
            print(row['salary'])

