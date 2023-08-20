numbers = list(map(int, input().split(", ")))
groups = 10
list_of_groups = []

while len(numbers) != 0:
    for num in numbers:
        if num <= groups:
            list_of_groups.append(num)

    for unnecessary_numbers in list_of_groups:
        numbers.remove(unnecessary_numbers)
    print(f"Group of {groups}'s: {list_of_groups}")
    list_of_groups.clear()
    groups += 10
