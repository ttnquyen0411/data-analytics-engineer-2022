import csv
emp_no = []

with open('dept_manager.csv') as csvfile:
    data = csv.DictReader(csvfile)

    for row in data:
        if row['dept_no'] == "d008":
            emp_no.append(row['emp_no'])
    print(emp_no)


