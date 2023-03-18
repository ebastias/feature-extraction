import pandas as pd
import os

while True:
    # Define the start and end indices for each label
    label_names = ["jumping", "walking", "jogging_in_place", "jumping_jacks", "sit_ups", "jumping_2"]
    label_indexes = []

    for label in label_names:
        index_input = input("Input the start and end index separated by a space for %s: " % (label))
        indexes_values = index_input.split(" ")

        # Convert string to int values and create dict
        indexes = {
            "start": int(indexes_values[0]),
            "end": int(indexes_values[1])
        }

        # Append dictionary to array of dict
        label_indexes.append(indexes)


    labels = {label_names[x]: label_indexes[x] for x in range(len(label_names))}

    # Read the filename from terminal input
    complete_filename = input("Enter the name of the CSV file: ")

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

    # Construct the new filename with the prefix "downsampled_"
    path, filename = os.path.split(complete_filename)
    print(path, filename)
    new_filepath = path + "/labeled_" + filename

    # Save the updated DataFrame to a new CSV file
    df.to_csv(new_filepath, index=False)

    answer = input("Do you have more files to label? (y/n)")

    if answer == "n" or answer == "no":
        break