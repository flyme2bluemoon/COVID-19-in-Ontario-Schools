import csv
import matplotlib.pyplot as plt

school_list = {}
number_of_schools = 4828

with open("csv/schoolsactivecovid.csv", "r", encoding = "ISO-8859-1") as data:
    data_reader = csv.reader(data)
    for row in data_reader:
        if row[2] not in school_list:
            school_list[row[2]] = []
        if row[3] not in school_list[row[2]]:
            school_list[row[2]].append(row[3])

school_list.pop('school_board')

for row in school_list:
    school_list[row] = len(school_list[row])

school_list = {k: v for k, v in sorted(school_list.items(), key=lambda item: item[1], reverse=True)}

for row in school_list:
    print(row, school_list[row])

keys = school_list.keys()
values = school_list.values()
plt.bar(keys, values)
plt.show()