import os
import json

def format_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_data = f.read()
        print(file_path)
        data = json.loads(file_data)
        
    formatted_data = [f"{item['timestamp']} - {item['author']['username']}: {item['content']}\n" for item in data]
    
    return formatted_data



def write_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(data)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                formatted_data = format_data(file_path)
                
                new_file_path = os.path.splitext(file_path)[0] + '_formatted.log'
                write_to_file(new_file_path, formatted_data)

directory = 'D:\\Projects\\loldudeAI\\rawconversations\\discord'
process_directory(directory)
