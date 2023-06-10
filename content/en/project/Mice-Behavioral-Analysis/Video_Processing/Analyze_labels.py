import os
import csv

def process_csv_file(file_path):
    sum_col2 = 0
    sum_col3 = 0
    num_transitions_col2 = 0
    num_transitions_col3 = 0
    consecutive_ones_col2 = []
    consecutive_ones_col3 = []
    prev_value_col2 = None
    prev_value_col3 = None
    consecutive_ones_count_col2 = 0
    consecutive_ones_count_col3 = 0

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row

        for row in reader:
            col2 = int(row[1])
            col3 = int(row[2])
            sum_col2 += col2
            sum_col3 += col3

            if prev_value_col2 is not None and col2 != prev_value_col2 and col2 != 0:
                num_transitions_col2 += 1
                consecutive_ones_col2.append(consecutive_ones_count_col2)
                consecutive_ones_count_col2 = 0

            if prev_value_col3 is not None and col3 != prev_value_col3 and col3 != 0:
                num_transitions_col3 += 1
                consecutive_ones_col3.append(consecutive_ones_count_col3)
                consecutive_ones_count_col3 = 0

            if col2 == 1:
                consecutive_ones_count_col2 += 1

            if col3 == 1:
                consecutive_ones_count_col3 += 1

            prev_value_col2 = col2
            prev_value_col3 = col3

        # Add the last consecutive ones counts
        consecutive_ones_col2.append(consecutive_ones_count_col2)
        consecutive_ones_col3.append(consecutive_ones_count_col3)

    return sum_col2, sum_col3, num_transitions_col2, num_transitions_col3, consecutive_ones_col2, consecutive_ones_col3

def process_label_files(folder_path):
    label_files = [file for file in os.listdir(folder_path) if file.endswith('Labels.csv')]

    results = []
    for label_file in label_files:
        file_path = os.path.join(folder_path, label_file)
        sum_col2, sum_col3, num_transitions_col2, num_transitions_col3, consecutive_ones_col2, consecutive_ones_col3 = process_csv_file(file_path)
        results.append((label_file, sum_col2, sum_col3, num_transitions_col2, num_transitions_col3, consecutive_ones_col2[1:], consecutive_ones_col3[1:]))

    return results

def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['File', 'Sum of left', 'Sum of right', 'Transitions in left', 'Transitions in right', 'Consecutive 1s in left', 'Consecutive 1s in right'])

        for result in results:
            writer.writerow(result)


# Usage example
folder_path = 'C:/Users/dhers/Desktop/data_to_train'  # Replace with the actual folder path
output_file = 'C:/Users/dhers/Desktop/data_to_train/output.csv'  # Replace with the desired output file path

results = process_label_files(folder_path)
save_results_to_csv(results, output_file)

print(f'Results saved to {output_file}')



