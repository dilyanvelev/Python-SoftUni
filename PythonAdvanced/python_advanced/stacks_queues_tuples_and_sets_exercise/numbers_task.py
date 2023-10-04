first_set, second_set = {*input().split()}, {*input().split()}
n_line = int(input())

for _ in range(n_line):
    command = input()
    if "Add First" in command:
        numbers = command.split()[2:]
        first_set = first_set.union(numbers)

    elif "Add Second" in command:
        numbers = command.split()[2:]
        second_set = second_set.union(numbers)

    elif "Remove First" in command:
        numbers = command.split()[2:]
        for number in numbers:
            if number in first_set:
                first_set.remove(number)

    elif "Remove Second" in command:

        numbers = command.split()[2:]
        for number in numbers:
            if number in second_set:
                second_set.remove(number)
    else:

        print('True' if first_set.issubset(second_set) or second_set.issubset(first_set) else 'False')

print(", ".join(map(str, sorted(map(int, first_set)))))
print(", ".join(map(str, sorted(map(int, second_set)))))
