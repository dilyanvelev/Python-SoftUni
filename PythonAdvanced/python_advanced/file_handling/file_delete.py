from os import remove

try:
    file_path = './my_first_file.txt'
    remove(file_path)

except FileNotFoundError:
    print("File already deleted!")