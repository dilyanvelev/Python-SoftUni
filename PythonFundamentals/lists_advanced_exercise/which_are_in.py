first_list = input().split(", ")
second_list = input().split(", ")
final_list = []


for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word:
            if first_word in final_list:
                continue
            final_list.append(first_word)
print(final_list)
