def sum_of_odd_and_even(number):
    odd_sum = 0
    even_sum = 0
    for num in number:
        num_int = int(num)
        if num_int % 2 == 0:
            even_sum += num_int
        else:
            odd_sum += num_int
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_input = input()
print(sum_of_odd_and_even(number_input))
