def print_percentages(wrestler_data):
    total_fights = float(wrestler_data["Wins"]) + float(wrestler_data["Losses"]) + float(wrestler_data["Draws"])
    percentage_wins = (float(wrestler_data["Wins"]) / float(total_fights)) * 100.0

    percentage_losses = (float(wrestler_data["Losses"]) / float(total_fights)) * 100.0

    percetage_draws = (float(wrestler_data["Draws"]) / float(total_fights)) * 100-0

    print(f'{wrestler_data["Wrestler"]} fought {total_fights} fights, with a {percentage_wins} of wins, {percentage_losses} of losses and {percetage_draws} draws')

import os
import csv

csv_path = os.path.join("C:\\Users\\lsauc\\Documents\\BootCamp\\Week3_Class3_Activities","Resources_WWE-Data-2016.csv")

name_to_check = input("Select a wrestler name") 
with open(csv_path, newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    next(csv_reader, None)# skips the first row (Headers)

    for row in csv_reader:
        if name_to_check == row[0]:
            wrestler = {
                "Wrestler": row[0],
                "Wins": row[1],
                "Losses": row[2],
                "Draws": row[3]
            }
            print_percentages(wrestler)
