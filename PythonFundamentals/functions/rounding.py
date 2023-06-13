# list_of_numbers = list(map(float, input().split()))
# rounded_list = []
# for num in list_of_numbers:
#     rounded_list.append(round(num))
# print(rounded_list)

print(list(map(lambda x: round(float(x)), input().split())))
