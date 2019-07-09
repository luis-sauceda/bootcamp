# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csv_path = os.path.join("C:\\Users\\lsauc\\Documents\\BootCamp\\Week3_Class3_Activities","Resources_cereal_bonus.csv")

with open(csv_path, newline='', encoding = 'unicode') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    #next(csv_reader, None)# skips the first row (Headers)

    for row in csv_reader:
        if float(row[7]) >= 5:
            print (row)
