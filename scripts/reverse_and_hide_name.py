import os
import re

def reverse(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines.reverse()
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def rev(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'): 
            file_path = os.path.join(directory_path, filename)
            reverse(file_path)

rev(r'D:\Projects\loldudeAI\raw\discord')
