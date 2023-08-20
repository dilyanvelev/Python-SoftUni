from collections import deque

petrol_pumps = int(input())
pumps = deque()
original_pumps = deque()

for pump in range(petrol_pumps):
    pump_details = [int(x) for x in input().split()]
    pumps.append(pump_details)
    original_pumps.append(pump_details)

count_stops = 0
total_liters = 0

while pumps:
    if count_stops == len(pumps):
        first_start = pumps[0]
        start_position = original_pumps.index(first_start)
        print(start_position)
        break
    for position in range(petrol_pumps):
        liters = pumps[position][0]
        kms = pumps[position][1]
        total_liters += liters
        if total_liters >= kms:
            total_liters -= kms
            count_stops += 1

        else:
            rotated = pumps.popleft()
            pumps.append(rotated)
            count_stops = 0
            total_liters = 0
            break