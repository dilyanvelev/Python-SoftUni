split_elements = []
elements_list = []
route = input().split("||")
amount_of_fuel = int(input())
ammunition = int(input())

for element in route:
    elements_list = element.split(" ")
    split_elements.append(elements_list)

split_elements.pop()
is_successful = True
for command, num in split_elements:
    num = int(num)
    if command == "Travel":

        amount_of_fuel = amount_of_fuel - num
        if amount_of_fuel > 0:
            print(f"The spaceship travelled {num} light-years.")
        else:
            print("Mission failed.")
            is_successful = False
            break
    elif command == "Enemy":

        if ammunition >= num:
            ammunition -= num
            print(f"An enemy with {num} armour is defeated.")
        elif ammunition <= num:
            if amount_of_fuel >= num * 2:
                amount_of_fuel -= num * 2
                print(f"An enemy with {num} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                is_successful = False
                break
    elif command == "Repair":
        ammunition += num * 2
        amount_of_fuel -= num
        print(f"Ammunitions added: {num * 2}.")
        print(f"Fuel added: {num}.")

if is_successful:
    print("You have reached Titan, all passengers are safe.")
