num = int(input())
for number in range(1, num + 1):
    sum_of_digits = 0
    number = str(number)
    for digit in number:
        sum_of_digits += int(digit)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")


