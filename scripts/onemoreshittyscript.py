import os

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            parts = line.split(':')
            if any(char.isalnum() for char in parts[-1].strip()):
                file.write(line)

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            process_file(os.path.join(root, file))

process_directory(r'D:\Projects\loldudeAI\raw')
