fire_data = input().split("#")
water = int(input())

cells_put_out = []
total_effort = 0
total_fire = 0

for fire_cell in fire_data:
    fire_type, cell_value = fire_cell.split(" = ")
    cell_value = int(cell_value)

    if fire_type == "High" and 81 <= cell_value <= 125:
        if water >= cell_value:
            water -= cell_value
            effort = 0.25 * cell_value
            total_effort += effort
            total_fire += cell_value
            cells_put_out.append(cell_value)

    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        if water >= cell_value:
            water -= cell_value
            effort = 0.25 * cell_value
            total_effort += effort
            total_fire += cell_value
            cells_put_out.append(cell_value)

    elif fire_type == "Low" and 1 <= cell_value <= 50:
        if water >= cell_value:
            water -= cell_value
            effort = 0.25 * cell_value
            total_effort += effort
            total_fire += cell_value
            cells_put_out.append(cell_value)

print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
