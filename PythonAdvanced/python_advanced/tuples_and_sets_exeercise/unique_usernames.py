n_lines = int(input())
usernames = set()
for _ in range(n_lines):
    username = input()
    usernames.add(username)

for username in usernames:
    print(username)