# Solomon Batenhorst
def binary_string(a_list, index):
    """ this function is recursion for binary string """
    if index == len(a_list):
        print("".join(a_list))
    else:
        if a_list[index] == "?":
            for i in ["0", "1"]:
                a_list[index] = i
                binary_string(a_list, index + 1)
                a_list[index] = "?"
        else:
            binary_string(a_list, index + 1)


def main():
    """ this is main and it runs the program """
    pattern = ['?', '0', '1', '?']
    print("Patter A:", ''.join(pattern))
    binary_string(pattern, 0)
    print()

    pattern_a = ['?', '?', '?', '?']
    print("Patter B:", ''.join(pattern_a))
    binary_string(pattern_a, 0)
    print()


if __name__ == '__main__':
    main()
