budget = float(input())
one_kg_flour = float(input())
colored_eggs = 0
loaf_count = 0

one_pack_eggs_price = one_kg_flour * 0.75
one_liter_milk = one_kg_flour * 1.25
milk_for_one_loaf = one_liter_milk * 0.25
products_for_one_loaf = one_pack_eggs_price + one_kg_flour + milk_for_one_loaf

while budget > 0:
    if budget - products_for_one_loaf > 0:
        budget -= products_for_one_loaf
        loaf_count += 1
        colored_eggs += 3

        if loaf_count % 3 == 0:
            colored_eggs -= loaf_count - 2

    else:
        break
print(f'You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
