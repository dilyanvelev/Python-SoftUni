number = int(input())
matrix = []
for _ in range(number):
    matrix.append([x for x in [int(x) for x in input().split(', ')] if x % 2 == 0])

print(matrix)
