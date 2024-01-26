def filter_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if ':' in line:
                outfile.write(line)

filter_file(r'D:\Projects\loldudeAI\raw\discord\13.txt', r'D:\Projects\loldudeAI\raw\discord\13_.txt')