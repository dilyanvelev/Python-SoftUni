#
# number_n = int(input())
# stack = []
# for _ in range(number_n):
#     command = input()
#
#     if command[0] == '1':
#         stack.append(int(command.split()[1]))
#     elif command[0] == '2':
#         if stack:
#             stack.pop()
#     elif command[0] == '3':
#         if stack:
#             print(max(stack))
#
#     else:
#         if stack:
#             print(min(stack))
#
# stack_len = len(stack)
# for index in range(stack_len):
#     spacing = ', ' if index < stack_len - 1 else ""
#     print(str(stack.pop()) + spacing, end='')
from collections import deque

number_n = int(input())
stack = deque()
for _ in range(number_n):
    query = input()

    if len(query) > 1:
        query_split = query.split()
        num = int(query_split[1])
        stack.append(num)
    elif len(query) == 1:
        if query == "2":
            if stack:
                stack.pop()
            continue
        elif query == "3":
            if stack:
                print(max(stack))
        elif query == "4":
            if stack:
                print(min(stack))
for i in range(len(stack)):
    last_digit = str(stack.pop())
    if i == 0:
        print(last_digit, end="")
    else:
        print(', ' + last_digit, end="")

