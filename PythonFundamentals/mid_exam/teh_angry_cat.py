price_rating = input().split(', ')
entry_point = int(input())
item_type = input()
price_rating.pop(entry_point)
string_left_part = "Left"
string_right_part = "Right"

left_part = list(map(int, price_rating[:entry_point]))
right_part = list(map(int, price_rating[entry_point:]))




# sum_left_part = sum(left_part)
# sum_right_part = sum(right_part)
# if sum_left_part == sum_right_part:
#     print(f"{string_left_part} - {sum_left_part}")
# else:
#     if sum_left_part > sum_right_part:
#         print(f'{string_left_part} - {sum_left_part}')
#     elif sum_left_part < sum_right_part:
#         print(f'{string_right_part} - {sum_right_part}')
# print(sum(left_part))
# print(sum(right_part))
# print(max(sum(left_part), sum(right_part)))
