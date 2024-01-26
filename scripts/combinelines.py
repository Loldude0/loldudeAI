import os
import re

def process_files(directory):
    pattern = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2} - .+: .+')
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                lines = f.readlines()

            combined_lines = []
            for line in lines:
                if pattern.match(line):
                    combined_lines.append(line.strip())
                else:
                    last_line_parts = combined_lines[-1].split(':', 1)
                    line_parts = line.strip().split(':', 1)
                    if len(last_line_parts) > 1 and len(line_parts) > 1:
                        combined_lines[-1] = last_line_parts[0] + ':' + last_line_parts[1] + ' ' + line_parts[1]
                    else:
                        combined_lines[-1] += ' ' + line.strip()

            with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
                for line in combined_lines:
                    f.write(line + '\n')

process_files('D:\\Projects\\loldudeAI\\rawconversations\\discord')
