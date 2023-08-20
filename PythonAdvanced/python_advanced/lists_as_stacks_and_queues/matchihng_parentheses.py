some_expression = input()
opening_parentheses_list = []

for index in range(len(some_expression)):
    char = some_expression[index]

    if char == '(':
        opening_parentheses_list.append(index)

    elif char == ')':
        first_index = opening_parentheses_list.pop()
        output_expr = some_expression[first_index:index + 1]

        print(output_expr)
