numbers = list(map(float, input().split()))
uniques = []
for number in numbers:

    if number not in uniques:
        print(f"{number:.1f} - {numbers.count(number)} times")
    uniques.append(number)
