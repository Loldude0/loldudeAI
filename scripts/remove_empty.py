import os
import re

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
                                if message.strip() and re.search('[a-zA-Z]', message):
                                    f.write(timestamp + ' - ' + author + ': ' + message)
                    f.truncate()

process_files(r'D:\Projects\loldudeAI\rawconversations')
