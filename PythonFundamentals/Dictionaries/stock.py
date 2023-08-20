inventory = input().split()
# ['cheese', '10', 'bread', '5', 'ham', '10', 'chocolate', '3']

bakery = {inventory[i]: int(inventory[i + 1]) for i in range(0, len(inventory), 2)}
# {'cheese': 10, 'bread': 5, 'ham': 10, 'chocolate': 3}
following_line = input().split()

for product in following_line:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
