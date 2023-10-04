def operations(a, b, operand):
    if operand == "/":
        return f"{a/b:.2f}"

    if operand == "*":
        return f"{a*b:.2f}"
    if operand == "-":
        return f"{a-b:.2f}"
    if operand == "+":
        return f"{a+b:.2f}"
    if operand == "^":
        return f"{a**b:.2f}"
