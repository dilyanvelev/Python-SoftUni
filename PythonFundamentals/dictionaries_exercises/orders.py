dictionary = {}
while True:
    command = input()
    if command == "buy":
        break

    product_info = command.split(" ")

    product = product_info[0]
    price = float(product_info[1])
    quantity = int(product_info[2])

    if product not in dictionary:
        dictionary[product] = dict(price=price, quantity=quantity)
    else:
        dictionary[product]['price'] = price
        dictionary[product]['quantity'] += quantity

for key, value in dictionary.items():
    total_price = 1
    for value1 in value.values():
        total_price *= value1
    print(f"{key} -> {total_price:.2f}")
