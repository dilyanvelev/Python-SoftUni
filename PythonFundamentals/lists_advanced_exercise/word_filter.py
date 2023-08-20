some_text = input().split()
even_length_list = [even_word for even_word in some_text if len(even_word) % 2 == 0]
print("\n".join(even_length_list))
