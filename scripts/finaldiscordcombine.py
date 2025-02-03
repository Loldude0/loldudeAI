import os
import glob
from datetime import datetime, timedelta

def combine_messages(directory):
    for filename in glob.glob(os.path.join(directory, '*')):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        combined_lines = []
        prev_author = None
        combined_message = ""
        prev_timestamp = None

        for line in reversed(lines):
            try:
                timestamp, message = line.split(' - ', 1)
                author, message = message.split(': ', 1)
            except ValueError:
                continue

            try:
                current_timestamp = datetime.fromisoformat(timestamp.strip())
            except ValueError:
                continue

            if prev_author == author and prev_timestamp - current_timestamp <= timedelta(minutes=120):
                combined_message = message.rstrip() + " " + combined_message
            else:
                if prev_author is not None:
                    combined_lines.append(f"{prev_timestamp} - {prev_author}: {combined_message.strip()}")
                combined_message = message.rstrip()
                prev_author = author
                prev_timestamp = current_timestamp

        if prev_author is not None:
            combined_lines.append(f"{prev_timestamp} - {prev_author}: {combined_message.strip()}")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write("\n".join(reversed(combined_lines)))

combine_messages(r"D:\Projects\loldudeAI\raw\discord")
combine_messages(r"D:\Projects\loldudeAI\raw\whatsapp")

