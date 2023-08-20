result = True
parentheses = input()
stack = []

for p in parentheses:
    if p in ["{", "[", "("]:
        stack.append(p)
    elif p == '}':
        if stack and stack[-1] == "{":
            if stack:
                stack.pop()
        else:
            result = False
            break
    elif p == "]":
        if stack and stack[-1] == "[":
            if stack:
                stack.pop()
        else:
            result = False
            break
    elif p == ")":
        if stack and stack[-1] == "(":
            if stack:
                stack.pop()
        else:
            result = False
            break

print('YES' if result else 'NO')

