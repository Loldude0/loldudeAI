import os
import datetime

def convert_to_iso8601(time_str):
    # Convert the time string to a datetime object
    dt = datetime.datetime.strptime(time_str, "%m/%d/%y, %I:%M %p")
    # Convert the datetime object to an ISO 8601 string with a zero offset
    return dt.strftime("%Y-%m-%dT%H:%M:%S.000000+00:00")

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            # Split the line into time, author, and message
            time_str, rest = line.split(' - ', 1)
            # Convert the time string to ISO 8601 format
            iso_time_str = convert_to_iso8601(time_str)
            # Write the line back to the file with the new time format
            file.write(f"{iso_time_str} - {rest}")

def process_directory(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Process each file in the directory
            process_file(os.path.join(root, file))

# Start the processing
process_directory("D:\\Projects\\loldudeAI\\rawconversations\\whatsapp")
