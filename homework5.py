import csv

with open('dept_emp.csv') as csvfile:
    data = csv.DictReader(csvfile)

    count_emp_d001 = 0

    for row in data:
        if row['dept_no'] == "d001":
            count_emp_d001 +=1
        else:
            break

    print(f"total employees of d001: {count_emp_d001}")

