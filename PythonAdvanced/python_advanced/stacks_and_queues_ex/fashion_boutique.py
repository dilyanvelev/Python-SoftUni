clothes = list(map(int, input().split()))
capacity = int(input())

racks = 0
temp = 0
for _ in range(len(clothes)):
    if temp + clothes[-1] > capacity:
        racks += 1
        temp = clothes[-1]
        if clothes:
            racks += 1

    elif temp + clothes[-1] == capacity:
        