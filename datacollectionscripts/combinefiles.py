import os

base_dir = r'D:\Projects\loldudeAI\rawconversations\discord'

for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)
    
    if os.path.isdir(subdir_path):
        # Create a new .txt file named after the subdirectory
        with open(os.path.join(base_dir, f'{subdir}.txt'), 'w', encoding='utf-8') as outfile:
            i = 1
            while True:
                file = os.path.join(subdir_path, f'{i}_formatted.log')
                # Check if the file exists
                if os.path.isfile(file):
                    # Open the .log file and append its contents to the .txt file
                    with open(file, 'r', encoding='utf-8') as infile:
                        lines = infile.readlines()
                        outfile.write(''.join(lines) + '\n')
                    i += 1
                else:
                    break
