text1_path = './text1.txt'
output_path = './output.txt'
words_path = './words.txt'
words_dict = {}

with open(words_path) as file:
    for line in file:
        words = line.split()
        for word in words:
            words_dict[word] = 0
with open(text1_path) as file1:
    for key, value in words_dict.items():
        for line1 in file1:
            if key.lower() in line1.lower():
                words_dict[key] += 1
        file1.seek(0)

words_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1]))

with open(output_path, 'w') as file_output:
    for key, value in words_dict.items():
        file_output.write(f"{key} - {value}" + '\n')
