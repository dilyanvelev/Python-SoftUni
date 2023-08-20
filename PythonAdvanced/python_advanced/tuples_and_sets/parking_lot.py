n_lines = int(input())
unique_plates = set([])
for _ in range(n_lines):

    direction, plate = input().split(', ')

    if direction == "IN":
        unique_plates.add(plate)
    elif direction == "OUT":
        unique_plates.remove(plate)

if unique_plates:
    for plate in unique_plates:
        print(plate)

else:
    print("Parking Lot is Empty")

