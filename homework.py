import csv
count = 0

with open('employees.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'],row['last_name'])
        count = count + 1
        if count >= 10:
            break