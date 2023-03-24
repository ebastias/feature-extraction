import pandas as pd
import numpy 
from scipy.signal import find_peaks
import os

while True:
    # Read the filename from terminal input
    complete_filename = input("Enter the name of the \"labeled\" CSV file to get the cadence: ")

    # Load data from CSV file
    df = pd.read_csv(complete_filename)

    # Convert the time column to datetime objects
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S.%f')

    # extract the numerical representation of the time
    df['time'] = df['time'].dt.hour + df['time'].dt.minute / 60 + df['time'].dt.second / 3600

    # Group data by label
    grouped = df.groupby('label')

    # Create a list to store the extracted features
    features = []

    # Loop through each group
    for label, group in grouped:

        # Calculate the magnitude of the accelerometer data
        group['mag'] = numpy.sqrt(group['acc_x']**2 + group['acc_y']**2 + group['acc_z']**2)

        # Set a threshold value for peak detection
        threshold = 1.0

        group = group.reset_index()

        # Detect peaks in the magnitude data
        peaks, _ = find_peaks(group['mag'], height=threshold)

        # Map the peak indices to the actual index of the row in the original dataframe
        peak_indexes = group['index'][peaks]

        # Calculate the time between adjacent peaks using the original index
        peak_times = df.loc[peak_indexes, 'time']
        # Calculate the time between adjacent peaks
        # peak_times = group['time'][peaks]
        cadence = 60 / numpy.mean(numpy.diff(peak_times))
        features.append({'label': label, 'cadence': cadence})

        # Print the cadence value
        print(f"Cadence {label}: {cadence:.2f}")

    # Convert the features list to a dataframe
    features_df = pd.DataFrame(features)

    path, filename = os.path.split(complete_filename)
    new_filepath = path + "/cadence_" + filename

    # Save the dataframe to a CSV file
    features_df.to_csv(new_filepath, index=False)

    # Ask the user if there are more files to analyze
    answer = input("Do you have more files to find the cadence for? (y/n)")

    if answer == "n" or answer == "no":
        break