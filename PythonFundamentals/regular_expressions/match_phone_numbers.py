import re

phone_number = input()

pattern = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"

valid_phone_numbers = re.findall(pattern, phone_number)

print(', '.join(valid_phone_numbers))
