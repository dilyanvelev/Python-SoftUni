chaos_of_chars = input()
digits = ""
letters = ""
symbols = ""

for char in chaos_of_chars:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        symbols += char

print(digits)
print(letters)
print(symbols)
