import csv
import datetime

with open('employees.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    count = 0


    for row in reader:
        if count <= 10:
            print(f"{row['first_name']} - {row['last_name']}")
            count += 1
        else:
            break