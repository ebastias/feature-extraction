import pandas as pd
import os
from utils.index_gathering import create_label_dict

while True:

    labels = create_label_dict()

    # Read the filename from terminal input
    complete_filename = input("Enter the name of the CSV file to label: ")

    if len(complete_filename) == 0 or complete_filename == None:
        print('No filename was given')
        break

    # Read in the CSV file
    df = pd.read_csv(complete_filename)

    # Add a new column called "label" with empty values
    df["label"] = ""

    # Loop through each label and update the label column in the DataFrame
    for label, index_range in labels.items():
        start = index_range["start"]
        end = index_range["end"]
        df.loc[start:end, "label"] = label

    # Construct the new filename with the prefix "labeled_"
    path, filename = os.path.split(complete_filename)
    print(path, filename)
    new_filepath = path + "/labeled_" + filename

    # Save the updated DataFrame to a new CSV file
    df.to_csv(new_filepath, index=False)

    answer = input("Do you have more files to label? (y/n)")

    if answer == "n" or answer == "no":
        break