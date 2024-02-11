import csv

def append_csv(source_csv, destination_csv):
    with open(source_csv, 'r') as source_file:
        csv_reader = csv.reader(source_file)
        data_to_append = list(csv_reader)

    with open(destination_csv, 'a', newline='') as destination_file:
        csv_writer = csv.writer(destination_file)
        csv_writer.writerows(data_to_append)

# Example usage:
source_file_path = 'output1.csv'
destination_file_path = 'output2.csv'

append_csv(source_file_path, destination_file_path)
