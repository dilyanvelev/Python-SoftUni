string_numbers = input().split()
n = int(input())
integer_numbers = []

for num in string_numbers:
    integer_numbers.append(int(num))
for _ in range(n):
    integer_numbers.remove(min(integer_numbers))
print(*integer_numbers, sep=", ")
