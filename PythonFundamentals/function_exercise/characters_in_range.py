def get_characters(first_character, second_character):
    collected_character = []
    for current_character in range(ord(first_character) + 1, ord(second_character)):
        collected_character.append(chr(current_character))
    return collected_character


first_character = input()
second_character = input()
result = get_characters(first_character,second_character)
print(' '.join(result))