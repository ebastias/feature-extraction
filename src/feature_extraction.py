import pandas as pd
import numpy
import os

while True:

    # Read the filename from terminal input
    complete_filename = input("Enter the name of the CSV file: ")

    if len(complete_filename) == 0 or complete_filename == None:
        print('No filename was given')
        break

    # Load data from CSV file
    data = pd.read_csv(complete_filename)

    # Group data by label
    grouped = data.groupby('label')

    # Window size defined to 25 because 12.5Hz x 2s = 25 rows
    window_size = 25

    # Create a list to store the extracted features
    features = []

    # Loop through each group
    for label, group in grouped:
        
        # Calculate the total number of windows for the group
        num_windows = int(numpy.ceil(len(group) / window_size))
        
        # Loop through each window
        for i in range(num_windows):
            
            # Calculate the start and end indices for the window
            start = i * window_size
            end = start + window_size
            
            # Extract the accelerometer data for the window
            window_data = group.iloc[start:end][['acc_x', 'acc_y', 'acc_z']]
            
            # Calculate the mean and standard deviation for the window
            mean = window_data.mean()
            std = window_data.std()
            
            # Add the label and features to the list
            features.append([label, mean['acc_x'], mean['acc_y'], mean['acc_z'], std['acc_x'], std['acc_y'], std['acc_z']])
            
    # Create a DataFrame from the list of features
    columns = ['label', 'mean_acc_x', 'mean_acc_y', 'mean_acc_z', 'std_acc_x', 'std_acc_y', 'std_acc_z']
    features_df = pd.DataFrame(features, columns=columns)


    # Construct the new filename with the prefix "feature_extraction"
    path, filename = os.path.split(complete_filename)
    print(path, filename)
    new_filepath = path + "/feature_extraction_" + filename

    # Export the DataFrame to a CSV file
    features_df.to_csv(new_filepath, index=False)

    # Ask the user if there are more files to analyze
    answer = input("Do you have more files to analyze? (y/n)")

    if answer == "n" or answer == "no":
        break
