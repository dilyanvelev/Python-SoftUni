n = int(input())

command_even = 'even'
command_odd = 'odd'
command_negative = 'negative'
command_positive = 'positive'
numbers =[]
filtered_numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)

command = input()

for num in numbers:
    filter_command = (
        (command == command_even and num % 2 == 0) or
        (command == command_odd and num % 2 != 0) or
        (command == command_positive and num >= 0) or
        (command == command_negative and num < 0)
    )
    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)


