text = input()
new_text = [chr(ord(char) + 3) for char in text]
print(''.join(new_text))
