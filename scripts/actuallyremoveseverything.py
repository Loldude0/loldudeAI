import os
import re

def remove_strings_in_files(directory, strings_to_remove):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            print(filepath)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            with open(filepath, 'w', encoding='utf-8') as file:
                for line in lines:
                    line = re.sub(r'http\S+', '', line)
                    line = re.sub(r'<\S+>', '', line)
                    line = re.sub(r'@\S+', '', line)
                    line = re.sub(r'{\S+}', '', line)
                    line = re.sub(r'[^\w\s\.\,\!\?\"\'\:\-\+\_]', '', line)
                    for string in strings_to_remove:
                        if string in line:
                            line = line.replace(string, '')
                    file.write(line)

directory = r'D:\Projects\loldudeAI\raw\whatsapp'
strings_to_remove = ['You deleted this message', '<Media omitted>']

remove_strings_in_files(directory, strings_to_remove)
