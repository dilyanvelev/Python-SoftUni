strings = input().split()
first_string = strings[0]
second_string = strings[1]
sum_of_order = 0
if len(first_string) >= len(second_string):
    if len(first_string) == len(second_string):
        # ['123', '522']
        for i in range(len(first_string)):
            sum_of_order += ord(first_string[i]) * ord(second_string[i])
    else:
        # ['George', 'Peter']
        diff = abs(len(first_string) - len(second_string))
        for i in range(len(first_string)):
            if i <= len(second_string) - diff:
                sum_of_order += ord(first_string[i]) * ord(second_string[i])
            else:
                sum_of_order += ord(first_string[i])
else:
    # first_string < second_string
    # ['a', 'aaaa']
    diff = abs(len(first_string) - len(second_string))
    for i in range(len(second_string)):
        if i < len(second_string) - diff:
            sum_of_order += ord(first_string[i]) * ord(second_string[i])
        else:
            sum_of_order += ord(second_string[i])
print(sum_of_order)