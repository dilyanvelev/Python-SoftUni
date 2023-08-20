n_lines = int(input())
unique_names = set([])
for _ in range(n_lines):
    name = input()
    unique_names.add(name)
for name in unique_names:
    print(name)
