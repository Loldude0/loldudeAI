import os

def delete_txt_files(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.txt'):
                file_path = os.path.join(foldername, filename)
                try:
                    os.remove(file_path)
                    print(f'Deleted {file_path}')
                except Exception as e:
                    print(f'Error while deleting file {file_path}. Reason: {str(e)}')

delete_txt_files(r'D:\Projects\loldudeAI\rawconversations\discord')
