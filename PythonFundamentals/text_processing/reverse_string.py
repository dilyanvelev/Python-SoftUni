some_text = ''

while some_text != 'end':
    some_text = input()
    if some_text != 'end':
        print(f'{some_text} = {some_text[::-1]}')