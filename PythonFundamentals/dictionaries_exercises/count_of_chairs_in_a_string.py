string = input()
no_spaces_string = string.replace(" ", "")

dictionary = {char: no_spaces_string.count(char) for char in no_spaces_string}

# for char in no_spaces_string:
#     if char not in dictionary:
#         dictionary[char] = 0
#     dictionary[char] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
