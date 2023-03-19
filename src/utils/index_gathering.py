import pandas as pd

def create_label_dict():
    label_dict = {
        "jumping": {"start": None, "end": None},
        "walking": {"start": None, "end": None},
        "jogging_in_place": {"start": None, "end": None},
        "jumping_jacks": {"start": None, "end": None},
        "sit_ups": {"start": None, "end": None},
        "jumping_2": {"start": None, "end": None}
    }
    # Read the filename from terminal input
    csv_filename = input("Enter the name of the CSV file with the labeling indexes: ")

    if len(csv_filename) == 0 or csv_filename == None:
        print('No filename was given')
        return

    df = pd.read_csv(csv_filename)


# iterate over the rows of the 'start' and 'end' columns simultaneously
    for index, row in df.iterrows():
        start_value = row['start']
        end_value = row['end']
        label = list(label_dict.keys())[index]
        label_dict[label]['start'] = start_value
        label_dict[label]['end'] = end_value

    print(label_dict)
    return label_dict
