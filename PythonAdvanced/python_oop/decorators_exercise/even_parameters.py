def even_parameters(func_ref):
    def wrapper(*args):
        flag = True
        for num in args:
            if not isinstance(num, int):
                flag = False
                break
            if num % 2 == 0:
                continue
            else:
                flag = False

        if flag:
            result = func_ref(*args)
            return result
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
