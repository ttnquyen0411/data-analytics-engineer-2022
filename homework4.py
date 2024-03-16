import csv

with open('employees.csv') as csvfile:
    data = csv.DictReader(csvfile)

    list_groupby_emp = []

    for row in data:
        if row['gender'] == "M":
            count_male += 1
        else:
            count_female +=1

    print(f"total male employees : {count_male}")
    print(f"total female employees : {count_female}")


