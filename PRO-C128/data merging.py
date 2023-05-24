import csv 
import pandas as pd 

file1="bright_stars.csv"
file2="dwarf_stars.csv"

with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        file1.append(row)

with open("archive_dataset_sorted1.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        file2.append(row)

headers_1 = file1[0]
planet_data_1 = file2[1:]

headers_2 = file2[0]
planet_data_2 = file2[1:]

headers = headers_1 + headers_2
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)