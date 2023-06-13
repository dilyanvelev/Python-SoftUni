animals = input()
animals_list = animals.split(', ')
animals_list = animals_list[::-1]

for i, item in enumerate(animals_list):
    if i == 0 and item == 'wolf':
        print('Please go away and stop eating my sheep')
    elif item == 'wolf' and i > 0:
        print(f'Oi! Sheep number {i}! You are about to be eaten by a wolf!')