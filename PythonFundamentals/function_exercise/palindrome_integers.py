def palindrome_check(numbers):
    for number in numbers:
        if number == number[::-1]:
            print(True)
        else:
            print(False)

    return ''


list_of_numbers = input().split(", ")
print(palindrome_check(list_of_numbers))
