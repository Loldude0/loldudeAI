import os
import re

def remove_words_with_numbers(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            with open(filepath, 'w', encoding='utf-8') as file:
                for line in lines:
                    if ':' in line:
                        before_colon, after_colon = line.rsplit(':', 1)
                        words = after_colon.split()
                        words = [word for word in words if len(re.findall(r'\d', word)) <= 4]
                        line = before_colon + ':' + ' '.join(words)
                    file.write(line + '\n')

directory = r'D:\Projects\loldudeAI\rawconversations'

remove_words_with_numbers(directory)
