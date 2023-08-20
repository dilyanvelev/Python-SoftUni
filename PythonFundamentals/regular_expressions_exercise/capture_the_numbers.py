import re

line = input()

pattern = "\d+"

while True:
    if line:
        matches = re.findall(pattern, line)
        if matches:
            print(' '.join(matches), end=' ')

    else:
        break
    line = input()
