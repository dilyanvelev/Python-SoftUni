from collections import deque

clients = deque()

while True:
    line = input()
    if line == "End":
        break

    if line == "Paid":
        while clients:
            print(clients.popleft())
    else:
        clients.append(line)
print(f"{len(clients)} people remaining.")
