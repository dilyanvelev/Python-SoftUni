from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))
print(max(orders))
while True:
    if orders:
        client = orders[0]
        if food_quantity >= client:
            food_quantity -= client
            orders.popleft()
        else:
            print(f"Orders left: {' '.join(map(str, orders))}")
            break
    else:
        print("Orders complete")
        break
