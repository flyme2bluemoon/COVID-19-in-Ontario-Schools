import csv

school_list = []
number_of_schools = 4828

with open("csv/schoolsactivecovid.csv", "r", encoding = "ISO-8859-1") as data:
    data_reader = csv.reader(data)
    for row in data_reader:
        school = row[3] + "-" + row[2]
        if school not in school_list:
            school_list.append(school)

print(school_list)
print(f"Cumulative Schools with COVID-19: {len(school_list)}")
print(f"Total schools: {number_of_schools}")
print(f"Cumulative percentage of Schools with COVID-19: {round(((len(school_list)/number_of_schools)*100), 2)}%")