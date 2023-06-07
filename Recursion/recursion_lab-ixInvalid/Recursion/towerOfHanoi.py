def tower_of_hanoi(n, a, b, c):
    if n == 1:
        print(f'{"Move Disk 1 from " + a + " to " + c:^33}')

    else:
        tower_of_hanoi(n - 1, a, c, b)
        print(f'{"Move Disk " + str(n) + " from " + a + " to " + c:^33}')
        tower_of_hanoi(n - 1, b, a, c)


def main():
    """ this is main and it runs the program """
    print(f'{"[Tower of Hanoi Solver]":-^33}')
    user_input = int(input(f'{"Enter[DISK AMOUNT]: ":>26}'))
    print(f'{"":-^33}')

    print(tower_of_hanoi(user_input, 'A', 'B', 'C'))


if __name__ == '__main__':
    main()
