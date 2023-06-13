from collections import deque


bees = list(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = input().split()
total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        symbol = symbols[0]
        collected_nectar, bee = nectar.pop(), bees.popleft()

        if symbol == '+':
            total_honey += abs(bee + collected_nectar)

        elif symbol == '-':
            total_honey = abs(bee - collected_nectar)

        elif symbol == '*':
            total_honey += abs(bee * collected_nectar)

        else:
            if collected_nectar == 0 and bee == 0:
                continue
            total_honey += abs(bee / collected_nectar)

    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
