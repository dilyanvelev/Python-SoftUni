gifts = input().split()

while True:
    command = input().split()
    action = command[0]

    if action == "OutOfStock":
        gift = command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "None"

    elif action == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gift = command[1]
        gifts[-1] = gift

    elif action == "No":
        break

gifts = [gift for gift in gifts if gift != "None"]
print(" ".join(gifts))
