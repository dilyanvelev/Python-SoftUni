def grocery_store(**kwargs):
    new_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ''
    for receipt in new_kwargs:
        result += f"{receipt[0]}: {receipt[1]}" + "\n"

    return result


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
