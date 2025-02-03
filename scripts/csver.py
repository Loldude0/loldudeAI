import os
import csv

def process_files(directory):
    data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    lines = f.read().splitlines()
                    for i in range(7, len(lines)):
                        row = [lines[i].rsplit(': ', 1)[-1].strip()]
                        for j in range(1, 8):
                            row.append(lines[i-j].rsplit(': ', 1)[-1].strip())
                        data.append(row)
    return data

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['response', 'context', 'context/0', 'context/1', 'context/2', 'context/3', 'context/4', 'context/5', 'context/6'])
        writer.writerows(data)

directory = r"D:\Projects\loldudeAI\raw"
output_file = "D:\\Projects\\loldudeAI\\dataset\\dataset_three.csv"
data = process_files(directory)
write_to_csv(data, output_file)
