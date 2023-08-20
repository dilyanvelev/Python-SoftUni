import re

dates = input()
pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"

result = re.findall(pattern, dates)

# ('13', '/', 'Jul', '1928')
# ('10', '-', 'Nov', '1934')
# ('25', '.', 'Dec', '1937')
for date in result:
    day = date[0]
    month = date[2]
    year = date[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
