def loading(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]\nStill loading..."


bar_value = int(input())
print(loading(bar_value))
