some_string = list(input())
unique_letters = set()

for char in some_string:
    unique_letters.add(char)

listed_set = list(sorted(unique_letters))

for char in listed_set:
    print(f"{char}: {some_string.count(char)} time/s")

