first_set_len, second_set_len = tuple(map(int, input().split()))
first_set = set()
second_set = set()

for _ in range(first_set_len):
    number = int(input())
    first_set.add(number)
for _ in range(second_set_len):
    number = int(input())
    second_set.add(number)

result = first_set & second_set

for num in result:
    print(num)