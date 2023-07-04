items_input = input().split("|")
budget = float(input())

valid_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

new_prices = []
profit = 0

for item in items_input:
    item_type, item_price = item.split("->")
    item_price = float(item_price)

    if item_type in valid_prices and item_price <= valid_prices[item_type]:
        if budget >= item_price:
            budget -= item_price
            new_price = item_price + item_price * 0.4
            new_prices.append(new_price)
            profit += new_price - item_price

new_prices_formatted = " ".join([f"{price:.2f}" for price in new_prices])

print(new_prices_formatted)
print(f"Profit: {profit:.2f}")

if budget + sum(new_prices) >= 150.00:
    print("Hello, France!")
else:
    print("Not enough money.")
