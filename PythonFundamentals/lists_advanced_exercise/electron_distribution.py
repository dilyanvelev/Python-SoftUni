def distribute_electrons(num_electrons):
    shells = []
    shell_num = 1
    electrons_left = num_electrons

    while electrons_left > 0:
        max_electrons = 2 * shell_num ** 2

        if electrons_left >= max_electrons:
            shells.append(max_electrons)
            electrons_left -= max_electrons
        else:
            shells.append(electrons_left)
            electrons_left = 0

        shell_num += 1

    return shells


number_electrons = int(input())

filled_shells = distribute_electrons(number_electrons)
print(filled_shells)
