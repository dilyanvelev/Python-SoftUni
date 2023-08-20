from collections import deque

names = deque(input().split())
number_of_passes = int(input())

while len(names) != 1:
    for i in range(number_of_passes):
        popped_name = names.popleft()
        names.append(popped_name)
    kid_left = names.pop()
    print(f"Removed {kid_left}")
print(f"Last is {names[0]}")
