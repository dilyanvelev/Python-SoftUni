n_lines = int(input())
odd_set = set()
even_set = set()
for row in range(1, n_lines + 1):
    names = input()
    ascii_sum = 0
    for char in names:
        ascii_sum += ord(char)
    ascii_sum = ascii_sum // row
    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

if sum(odd_set) == sum(even_set):
    print(odd_set.union(even_set))
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
    print(', '.join(map(str, result)))
elif sum(odd_set) < sum(even_set):
    result = odd_set.symmetric_difference(even_set)
    print(', '.join(map(str, result)))
