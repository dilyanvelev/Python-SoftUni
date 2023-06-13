data = input().split()
products_dict = {}
for i in range(0, len(data), 2):
    products_dict[data[i]] = int(data[i + 1])

print(products_dict)
