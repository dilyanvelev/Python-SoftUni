def calculation_func(operator, number1, number2):
    if operator == "multiply":
        return number1 * number2
    elif operator == 'divide':
        return number1 // number2
    elif operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2


operator_type = input()
first_number = int(input())
second_number = int(input())
print(calculation_func(operator_type, first_number, second_number))
