numbers_of_rooms = int(input())
free_chairs_count = 0
for room_number in range(1, numbers_of_rooms + 1):
    chairs_and_visitors = input().split()
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])
    reminder = int(chairs) - int(visitors)
    free_chairs_count += reminder
    if chairs < visitors:
        diff = abs(int(chairs) - int(visitors))
        print(f"{diff} more chairs needed in room {room_number}")
if free_chairs_count >= 0:
    print(f"Game On, {free_chairs_count} free chairs left")
