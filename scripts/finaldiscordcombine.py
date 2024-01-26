import os
import glob

def combine_messages(directory):
    for filename in glob.glob(os.path.join(directory, '*')):
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        combined_lines = []
        prev_author = None
        combined_message = ""

        for line in reversed(lines):
            try:
                timestamp, message = line.split(' - ', 1)
                author, message = message.split(': ', 1)
            except ValueError:
                continue

            if author == prev_author:
                combined_message = message.rstrip() + " " + combined_message
            else:
                if prev_author is not None:
                    combined_lines.append(f"{timestamp} - {prev_author}: {combined_message.strip()}")
                combined_message = message.rstrip()
                prev_author = author

        if prev_author is not None:
            combined_lines.append(f"{timestamp} - {prev_author}: {combined_message.strip()}")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write("\n".join(reversed(combined_lines)))

combine_messages(r"D:\Projects\loldudeAI\rawconversations\discord")
