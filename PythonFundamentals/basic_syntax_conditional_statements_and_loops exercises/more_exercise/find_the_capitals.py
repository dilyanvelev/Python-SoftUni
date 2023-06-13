some_string = input()
upper_letters_list = []

for index, char in enumerate(some_string):
    if char.isupper():
        upper_letters_list.append(index)

print(upper_letters_list)
