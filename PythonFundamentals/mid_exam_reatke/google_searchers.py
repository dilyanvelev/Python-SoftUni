income = float(input())
users = int(input())
total_money = 0

for i in range(1, users + 1):
    number_of_searches = int(input())
    if i % 3 == 0:
        if number_of_searches > 5:
            new_income = income * 3
            total_money += number_of_searches * new_income * 2
        elif number_of_searches == 1:
            continue
        else:
            total_money += number_of_searches * income * 3

    else:
        if number_of_searches > 5:
            total_money += number_of_searches * income * 2
        elif number_of_searches == 1:
            continue
        else:
            total_money += number_of_searches * income

print(f"Total money earned: {total_money:.2f}")
