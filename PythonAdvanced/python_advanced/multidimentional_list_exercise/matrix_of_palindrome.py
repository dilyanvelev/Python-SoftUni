rows, cols = [int(x) for x in input().split()]
first_letter = 97
for row in range(rows):

    for col in range(cols):
        col += row
        palindrome_str = chr(first_letter + row) + chr(first_letter + col) + chr(first_letter + row)
        print(palindrome_str, end=' ')
    print()