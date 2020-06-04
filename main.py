import csv
with open("vocabulary.csv", newline='', encoding="utf-8") as file:
    csv_file = csv.reader(file, delimiter=",")
    for line in csv_file:
        print(line)