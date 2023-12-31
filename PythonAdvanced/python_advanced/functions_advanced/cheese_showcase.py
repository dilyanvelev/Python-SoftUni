def sorting_cheeses(**kwargs):
    kwargs_sort = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for key, value in kwargs_sort:
        sort_value = sorted(value, reverse=True)
        result += key + '\n'
        result += "\n".join([str(x) for x in sort_value]) + '\n'

    return result


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125]))
# ('Parmesan', [102, 120, 135])
# ('Camembert', [100, 100, 105, 500, 430])
# ('Mozzarella', [50, 125])
