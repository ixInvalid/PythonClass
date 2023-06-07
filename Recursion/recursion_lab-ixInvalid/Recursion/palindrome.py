import string


def palindrome(s):
    """ this function tells the user if their input is a palindrome """
    s = s.lower().replace(' ', '', ).translate(str.maketrans('', '', string.punctuation))

    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])


def main():
    """ this is main and it runs the program """
    print(f'{"[Palindrome Detector]":-^32}')
    user_input = input("Enter [ WORD | NUMBER | PHRASE ]: ").translate(str.maketrans('', '', string.punctuation))

    print(f'{"":-^32}')

    if palindrome(user_input):
        print(f'{user_input + " is a PALINDROME":^32}')
    else:
        print(f'{user_input + " is NOT a PALINDROME":^32}')


if __name__ == '__main__':
    main()
