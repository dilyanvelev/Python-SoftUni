def operate(operator, *args):
    result = args[0]

    for num in args[1:]:
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        elif operator == '/':
            result /= num

    return result


print(operate("*", 3, 4))
