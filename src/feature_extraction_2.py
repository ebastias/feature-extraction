import pandas as pd
import numpy
from scipy.signal import find_peaks
import os

# Create a list to store the extracted features
features = []
i = 0

while True:
    i += 1
    # Read the filename from terminal input
    complete_filename = input("Enter the name of the CSV file with the first feature extraction: ")

    if len(complete_filename) == 0 or complete_filename == None:
        print('No filename was given')
        break

    # Load data from CSV file
    data = pd.read_csv(complete_filename)

    # Group data by label
    grouped = data.groupby('label')

    # Loop through each group
    for label, group in grouped:
    
        # Calculate the mean and standard deviation for the group columns
        mean = group[['mean_acc_x', 'mean_acc_y', 'mean_acc_z', 'std_acc_x', 'std_acc_y', 'std_acc_z']].mean()
        newLabel = label + "_" + str(i)
                
        # Add the label and features to the list
        features.append([newLabel, mean['mean_acc_x'], mean['mean_acc_y'], mean['mean_acc_z'], mean['std_acc_x'], mean['std_acc_y'], mean['std_acc_z']])


    # Ask the user if there are more files to analyze
    answer = input("Do you have more files to analyze before exporting the feature extractions? (y/n)")

    if answer == "n" or answer == "no":            
        # Create a DataFrame from the list of features
        print("\nSaving file.\n")
        columns = ['label', 'mean_acc_x', 'mean_acc_y', 'mean_acc_z', 'std_acc_x', 'std_acc_y', 'std_acc_z']
        features_df = pd.DataFrame(features, columns=columns)


        # Construct the new filename with the prefix "feature_extraction"
        path, filename = os.path.split(complete_filename)
        print(path, filename)
        new_filepath = path + "/feature_extraction_2_complete.csv" 

        # Export the DataFrame to a CSV file
        features_df.to_csv(new_filepath, index=False)
        break
