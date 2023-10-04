from math_module.operations import operations

first_number, operator, second_number = input().split()

print(operations(float(first_number), int(second_number), operator))
