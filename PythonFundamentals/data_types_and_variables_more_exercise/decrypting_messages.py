key_number = int(input())
number_lines = int(input())
char_list = []
for char in range(number_lines):
    current_char = input()
    number_of_char = ord(current_char) + key_number
    char_list.append(chr(number_of_char))

print(''.join(char_list))
