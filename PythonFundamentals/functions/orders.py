def total_price(product: str, quantity: int):
    result = 0
    if product == 'coffee':
        result = 1.50 * quantity
    elif product == 'coke':
        result = 1.40 * quantity
    elif product == 'water':
        result = 1.00 * quantity
    elif product == 'snacks':
        result = 2.00 * quantity
    return result


product_type = input()
product_quantity = int(input())

print(f'{total_price(product_type, product_quantity):.2f}')
