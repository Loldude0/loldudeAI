import os
import re
import unicodedata

def remove_emojis_and_punctuation(input_string):
    # Remove emojis
    input_string = ''.join(c for c in input_string if not unicodedata.category(c).startswith('So'))

    # Remove punctuation
    input_string = re.sub(r'[^\w\s]', '', input_string)

    # Remove extra spaces
    input_string = re.sub(r'\s+', ' ', input_string)

    # Convert to lowercase
    input_string = input_string.lower()

    # Remove <some_number> pattern
    input_string = re.sub(r'<\d+>', '', input_string)

    return input_string

def process_files(directory):
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".txt"):
                with open(filepath, 'r+', encoding='utf-8') as f:
                    lines = f.readlines()
                    f.seek(0)
                    for line in lines:
                        parts = line.split(' - ', 1)
                        if len(parts) == 2:
                            timestamp, rest = parts
                            author_message = rest.split(': ', 1)
                            if len(author_message) == 2:
                                author, message = author_message
                                new_message = remove_emojis_and_punctuation(message)
                                f.write(timestamp + ' - ' + author + ': ' + new_message + '\n')
                    f.truncate()

process_files(r'D:\Projects\loldudeAI\rawconversations') 
