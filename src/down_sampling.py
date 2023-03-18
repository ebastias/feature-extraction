import pandas as pd
import os

while True:
    # Read the filename from terminal input
    complete_filename = input("Enter the name of the CSV file: ")

    if len(complete_filename) == 0 or complete_filename == None:
        print('No filename was given')
        break

    # Load the dataset
    data = pd.read_csv(complete_filename)

    # Set the new sampling rate to 12.5Hz
    new_sampling_rate = 2

    # Downsample the dataset
    downsampled_data = data.iloc[::new_sampling_rate, :]

    # Construct the new filename with the prefix "downsampled_"
    path, filename = os.path.split(complete_filename)
    print(path, filename)
    new_filepath = path + "/downsampled_" + filename

    # Save the downsampled dataset to a new CSV file with the new filename
    downsampled_data.to_csv(new_filepath, index=False)

    # Ask the user if there are more files to downsample
    answer = input("Do you have more files to downsample? (y/n)")

    if answer == "n" or answer == "no":
        break
