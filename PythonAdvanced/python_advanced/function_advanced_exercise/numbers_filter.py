def even_odd_filter(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        if key not in dictionary:
            dictionary[key] = []

        if key == 'odd':
            dictionary[key] = [i for i in value if i % 2 != 0]

        elif key == 'even':
            dictionary[key] = [i for i in value if i % 2 == 0]

    return dict(sorted(dictionary.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
