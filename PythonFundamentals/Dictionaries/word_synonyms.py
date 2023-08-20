n = int(input())
dict_of_words = {}
for _ in range(n):
    word = input()
    synonym = input()
    if word not in dict_of_words:
        dict_of_words[word] = []
    dict_of_words[word].append(synonym)

for word_as_key, synonyms_as_value in dict_of_words.items():
    print(f"{word_as_key} - {', '.join(synonyms_as_value)}")

