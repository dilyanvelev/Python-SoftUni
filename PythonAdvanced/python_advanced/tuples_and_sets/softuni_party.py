n_lines = int(input())
vip_list = set()
regular_list = set()

for _ in range(n_lines):
    guests = input()
    if guests[0].isdigit():
        vip_list.add(guests)
    else:
        regular_list.add(guests)

while True:
    guests = input()
    if guests == 'END':
        break
    if guests[0].isdigit():
        regular_list.add(guests)
    else:
        vip_list.add(guests)
without_them = sorted(regular_list.symmetric_difference(vip_list))
print(len(without_them))
for invite_code in without_them:
    print(invite_code)
