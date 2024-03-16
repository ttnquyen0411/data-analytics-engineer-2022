import csv
result = {}
total_salary = 0


with open("salaries.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp_no = row['emp_no']
        key = emp_no
        salary = int(row['salary'])
        if key not in result:
            result[key] = []
        result[key].append(salary)

        #print(key, result[key])

    salary_by_employee = {}
    for key in result:
        salary_by_employee[key] = sum(result[key])

        #print(key, salary_by_employee[key])

    for key in salary_by_employee:
        maximum = max(salary_by_employee, key=salary_by_employee.get)
    print(maximum,salary_by_employee[maximum])


