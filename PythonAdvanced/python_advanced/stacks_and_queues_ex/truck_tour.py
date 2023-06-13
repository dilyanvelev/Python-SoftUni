N = int(input())
total_fuel = 0
stops = 0

for _ in range(N):
    fuel, distance = input().split()
    total_fuel += int(fuel)

    if total_fuel >= int(distance):
        total_fuel -= int(distance)

    else:
        stops += 1
        total_fuel = 0

print(stops)
