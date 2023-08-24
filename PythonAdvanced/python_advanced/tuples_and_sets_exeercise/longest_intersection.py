n_line = int(input())
intersection = set()

for _ in range(n_line):
    right_side, left_side = input().split('-')
    first_start, first_end = map(int, right_side.split(','))
    second_start, second_end = map(int, left_side.split(','))
    first_set_check = set()
    second_set_check = set()

    for num in range(first_start, first_end + 1):
        first_set_check.add(num)
    for num in range(second_start, second_end + 1):
        second_set_check.add(num)

    intersection_check = first_set_check.intersection(second_set_check)

    if len(intersection) < len(intersection_check):
        intersection = intersection_check
intersection_list = []
for num in intersection:
    intersection_list.append(num)

print(f"Longest intersection is {sorted(intersection_list)} with length {len(intersection_list)}")
