file_path = 'files/text.txt'
symbols = ["-", ",", ".", "!", "?"]
new_lines = []
with open(file_path, 'r') as file:
    lines = file.readlines()

for row in range(0, len(lines), 2):
    for symbol in symbols:
        lines[row] = lines[row].replace(symbol, '@')

    print(*lines[row].split()[::-1])
