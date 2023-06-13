from collections import deque

colors = deque(input().split())
MAIN_COLORS = ['red', 'yellow', 'blue']
SECONDARY_COLORS = ['orange', 'purple', 'green']
final_colors = []

while colors:
    if len(colors) > 1:
        first, last = colors.popleft(), colors.pop()
        substring = first + last
        substring_2 = last + first
        if substring in MAIN_COLORS or substring_2 in SECONDARY_COLORS:
            final_colors.append(substring)
        elif substring_2 in MAIN_COLORS or substring_2 in SECONDARY_COLORS:
            final_colors.append(substring_2)

        else:
            first_stripped, last_stripped = first[:-1], last[:-1]

            if first_stripped:
                colors.insert(len(colors) // 2, first_stripped)
            if first_stripped:
                colors.insert(len(colors) // 2, last_stripped)
