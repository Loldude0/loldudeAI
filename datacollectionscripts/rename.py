import os

def rename_files(directory):
    total_lines = 0
    for count, filename in enumerate(os.listdir(directory)):
        dst = str(count + 1) + ".txt"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, dst)
        with open(src, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total_lines += len(lines)
        os.rename(src, dst)

    print(total_lines)

rename_files(r'D:\Projects\loldudeAI\rawconversations\discord')
rename_files(r'D:\Projects\loldudeAI\rawconversations\whatsapp')
