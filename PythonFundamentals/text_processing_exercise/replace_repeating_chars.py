input_string = input()
result = input_string[0]
for i in range(1, len(input_string)):
    if input_string[i] != input_string[i - 1]:
        result += input_string[i]
print(result)
