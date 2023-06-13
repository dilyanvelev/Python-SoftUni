number_of_messages = int(input())


for i in range(number_of_messages + 1):

    while i < number_of_messages:
        message_type = int(input())
        if message_type == 88:
            print('Hello')
            break

        elif message_type == 86:
            print('How are you?')
            break

        elif message_type != 88 and message_type != 86 and message_type < 88:
            print('GREAT!')
            break

        else:
            print('Bye.')
            break

