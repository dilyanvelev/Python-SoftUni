sums_list_as_str = input().split(', ')
count_of_beggars = int(input())
final_list = []
counter_of_index = 0
#sums_list_as_digits = [int(i) for i in sums_list]
sums_list_as_digits = []
for element in sums_list_as_str:
    sums_list_as_digits.append(int(element))
while counter_of_index < count_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(counter_of_index, len(sums_list_as_digits), count_of_beggars):
        sum_for_current_beggar += sums_list_as_digits[current_index]
    counter_of_index += 1
    final_list.append(sum_for_current_beggar)

print(final_list)
