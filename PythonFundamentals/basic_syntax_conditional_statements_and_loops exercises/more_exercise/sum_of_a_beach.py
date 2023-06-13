text = input()
text = text.lower()

text_list = ["sand", 'water', 'fish', 'sun']
counter = 0

for item in text_list:
    if item in text:
        word_count = text.count(item)
        counter += word_count

print(counter)
