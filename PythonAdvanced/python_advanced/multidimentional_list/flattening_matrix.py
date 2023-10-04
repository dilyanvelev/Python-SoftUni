number = int(input())

matrix = []

for _ in range(number):
    matrix.extend([int(x) for x in input().split(', ')])


print(matrix)
