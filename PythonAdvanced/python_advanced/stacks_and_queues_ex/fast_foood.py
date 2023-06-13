from collections import deque

quantity = int(input())

orders = deque(map(int, input().split()))

print(max(orders))

for _ in range(len(orders)):
    if orders[0] < quantity:
        quantity -= orders.popleft()

    else:
        break

if orders:
