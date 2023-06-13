mg_caffeine = list(map(int, input().split(", ")))  # 34, 2, 3
drinks = list(map(int, input().split(", ")))  # 40, 100, 250
# MAX_CAFF = 300
total_caffeine = 0

while True:
    last_mg_caff = mg_caffeine.pop()
    first_drink = drinks.pop(0)
    caffeine_sum = last_mg_caff * first_drink

    total_caffeine += caffeine_sum

    if total_caffeine > 300:
        total_caffeine -= caffeine_sum
        drinks.append(first_drink)
        if total_caffeine > 30:
            total_caffeine -= 30

    if len(drinks) == 0 or len(mg_caffeine) == 0:
        break

if drinks:
    print(f"Drinks left: {', '.join(str(x) for x in drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
