n_lines = int(input())
unique_elements = set()

for _ in range(n_lines):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

for element in unique_elements:
    print(element)
