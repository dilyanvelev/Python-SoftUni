secret_message = input().split()
deciphered_message = []

for word in secret_message:
    listed_word = list(word)
    first_three = listed_word[0] + listed_word[1] + listed_word[2]
    if first_three.isdigit():
        del listed_word[0:3]
        char_from_int = chr(int(first_three))
        listed_word.insert(0, char_from_int)
    first_two = listed_word[0] + listed_word[1]
    if first_two.isdigit():
        del listed_word[0:2]
        char_from_int = chr(int(first_two))
        listed_word.insert(0, char_from_int)
    listed_word[1], listed_word[-1] = listed_word[-1], listed_word[1]
    new_word = "".join(char for char in listed_word)
    deciphered_message.append(new_word)

print(" ".join(deciphered_message))
