clothes = list(map(int, input().split()))
capacity = int(input())
rack_counter = 1
temp = 0

for _ in range(len(clothes)):

    if temp + clothes[-1] > capacity:
        rack_counter += 1
        temp = clothes.pop()
    elif temp + clothes[-1] == capacity:
        temp = 0
        clothes.pop()
        if clothes:
            rack_counter += 1

    else:
        temp += clothes.pop()

print(rack_counter)