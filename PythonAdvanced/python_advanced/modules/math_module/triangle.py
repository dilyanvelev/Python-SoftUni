def triangle(number):
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

        # Print the bottom half of the pattern
    for i in range(number - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
