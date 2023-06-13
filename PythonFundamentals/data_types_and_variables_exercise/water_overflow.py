number_lines = int(input())
tank_filled = 0
counter = 0

while counter < number_lines:
    counter += 1
    liters_of_water = int(input())
    tank_filled += liters_of_water
    if tank_filled > 255:
        tank_filled -= liters_of_water
        print('Insufficient capacity!')
        continue


print(tank_filled)
