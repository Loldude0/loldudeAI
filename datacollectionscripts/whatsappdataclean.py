import os
import re
import unicodedata

directory = 'D:/Projects/loldudeAI/rawconversations/whatsapp'

def remove_emoji(string):
    return ''.join(c for c in string if not unicodedata.category(c).startswith('So'))

# Regular expression pattern to match the date, time, person and message format
pattern = re.compile(r'^(\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s(?:am|pm)\s-\s)(.*)(:.*$)')

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        new_lines = []
        current_person = None
        current_message = ""
        first_message = True
        for line in lines:
            if 'http' not in line and '<Media omitted>' not in line:
                match = pattern.match(line)
                if match:
                    person_name = match.group(2)
                    if person_name.lower() != 'loldude':
                        person_name = 'person'
                    message = match.group(3)
                    if current_person is None:
                        current_person = person_name
                        current_message = message
                    elif current_person == person_name:
                        current_message += " " + message[2:]  # remove the first two characters from subsequent messages
                    else:
                        line = match.group(1) + current_person + remove_emoji(current_message).replace('QWERTYGHOANV', 'loldude').lower()
                        new_lines.append(line)
                        current_person = person_name
                        current_message = message
        if current_person is not None:
            line = match.group(1) + current_person + remove_emoji(current_message).replace('QWERTYGHOANV', 'loldude').lower()
            new_lines.append(line)

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
