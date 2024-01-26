import os

base_dir = r'D:\Projects\loldudeAI\raw\discord'

for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)
    
    if os.path.isdir(subdir_path):
        with open(os.path.join(base_dir, f'{subdir}.txt'), 'w', encoding='utf-8') as outfile:
            i = 1
            while True:
                file = os.path.join(subdir_path, f'{i}_formatted.log')
                if os.path.isfile(file):
                    with open(file, 'r', encoding='utf-8') as infile:
                        lines = infile.readlines()
                        outfile.write(''.join(lines) + '\n')
                    i += 1
                else:
                    break
