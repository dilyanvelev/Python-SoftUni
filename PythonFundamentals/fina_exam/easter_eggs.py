import re


def easter_eggs():
    data = input()
    pattern = r'(\@+|#+)([a-z]{3,})(\@+|#+)|(\/+)([0-9]{1,})(\/+)'
    result = re.finditer(pattern, data)
    # words = {}
    colors_and_digits_list = []
    digits_list = []
    colors_list = []
    for res in result:
        word = res.group()
        # print(word)
        word = word.replace("/", '')
        word = word.replace("@", '')
        word = word.replace("#", '')
        colors_and_digits_list.append(word)
    for item in colors_and_digits_list:
        if item.isdigit():
            digits_list.append(item)

        else:
            colors_list.append(item)

    for color in colors_list:
        for num in digits_list:
            print(f'You found {num} {color} eggs!')
        break



    #print(colors_and_digits_list)


easter_eggs()
