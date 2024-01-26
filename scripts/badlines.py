import os
import datetime

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            try:
                datetime.datetime.strptime(line.split(' ', 1)[0].strip(), "%Y-%m-%dT%H:%M:%S.%f%z+00:00")
                file.write(line)
            except ValueError:
                print(f"Invalid time format in line: {line.strip()}")
                print(f"File: {file_path}")           

def process_directory(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            process_file(os.path.join(root, file))

process_directory(r"D:\Projects\loldudeAI\raw\whatsapp")