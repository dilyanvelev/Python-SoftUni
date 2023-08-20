countries = input().split(", ")
capitals = input().split(", ")
dictionary = {countries[index]: capitals[index] for index in range(len(capitals))}

for country, capital in dictionary.items():
    print(f"{country} -> {capital}")