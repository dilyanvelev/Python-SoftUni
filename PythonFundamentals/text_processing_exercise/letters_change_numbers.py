text = input().split()

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = ''
letters = ''
total_sum = []
for string in text:
    for char in string:
        if char.isdigit():
            digit += char
        else:
            letters += char
    digit = int(digit)
    if letters[0].isupper():
        index = alphabet_upper.index(letters[0]) + 1
        digit /= index

    else:
        index = alphabet_lower.index(letters[0]) + 1
        digit *= index

    if letters[1].isupper():
        index = alphabet_upper.index(letters[1]) + 1
        digit -= index
    else:
        index = alphabet_lower.index(letters[1]) + 1
        digit += index

    total_sum.append(digit)
    digit = ''
    letters = ''
print(f"{sum(total_sum):.2f}")