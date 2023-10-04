def even_odd(*args):
    command = args[-1]
    args = args[:-1]
    odd_list = []
    even_list = []
    for num in args:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    if command == "odd":
        return odd_list
    return even_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
