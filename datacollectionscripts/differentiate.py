import os
from datetime import datetime, timedelta

def process_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            with open(filepath, 'w', encoding='utf-8') as f:
                prev_time = None
                for line in lines:
                    timestamp_str, _, _ = line.partition(' - ')
                    curr_time = datetime.fromisoformat(timestamp_str)
                    if prev_time and curr_time - prev_time >= timedelta(hours=6):
                        f.write('\n')
                    f.write(line)
                    prev_time = curr_time

process_files('D:\\Projects\\loldudeAI\\rawconversations')
