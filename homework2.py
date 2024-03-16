import csv

with open('employees.csv') as csvfile:
    data = csv.reader(csvfile)

    for row in data:
        male_list = ["first_name", "last_name"]
        where = {"gender": "M"}

list_column_string = ",".join(male_list)

string = f"SELECT {list_column_string} FROM data WHERE 1 = 1"
print(f"sql string: {string}")