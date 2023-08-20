file_path = input().split("\\")
file = file_path[-1]
file_and_extension = file.split(".")
print(f"File name: {file_and_extension[0]}")
print(f"File extension: {file_and_extension[-1]}")
