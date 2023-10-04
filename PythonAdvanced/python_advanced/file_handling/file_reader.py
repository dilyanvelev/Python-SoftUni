file_path = "./numbers.txt"
numbers_sum = 0
with open(file_path, 'r') as file:
    for line in file:
        numbers_sum += int(line)

print(numbers_sum)
