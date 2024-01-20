import os
import re

def change_author_remove_parts_and_reverse_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    new_lines = []
    for line in lines:
        match = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}) - (\w+): (.*)', line)
        if match:
            timestamp, author, message = match.groups()
            if author != 'loldude0':
                author = 'person'
            message = re.sub(r'<\d+>', '', message)  # remove parts similar to <some numbers>
            message = re.sub(r'(\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}) - (\w+):', '', message)  # remove parts similar to 2_digits:2_digits.6_digits+00:00
            new_line = f'{timestamp} - {author}: {message}\n'
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    new_lines.reverse()
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def change_author_remove_parts_and_reverse_lines_in_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'): 
            file_path = os.path.join(directory_path, filename)
            change_author_remove_parts_and_reverse_lines_in_file(file_path)

change_author_remove_parts_and_reverse_lines_in_files_in_directory(r'D:\Projects\loldudeAI\rawconversations\discord')
