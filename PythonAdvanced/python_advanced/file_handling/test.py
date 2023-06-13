from os import remove

try:
    remove('./.txt')

except FileNotFoundError:
    print('File does not exist')

