numbers = list(map(int, input().split(", ")))

positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
positive_numbers_string = [str(str_num) for str_num in positive_numbers]
negative_numbers_string = [str(str_num) for str_num in negative_numbers]
even_numbers_string = [str(str_num) for str_num in even_numbers]
odd_numbers_string = [str(str_num) for str_num in odd_numbers]

print(f"Positive: {', '.join(positive_numbers_string)}")
print(f"Negative: {', '.join(negative_numbers_string)}")
print(f"Even: {', '.join(even_numbers_string)}")
print(f"Odd: {', '.join(odd_numbers_string)}")
