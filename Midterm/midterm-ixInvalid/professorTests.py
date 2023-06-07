# Solomon Batenhorst
from professor import *


def test_constructor():
    """ this function tests the constructor of a professor object """
    test_default = Professor()

    print(f'{"[Constructor Test]":-^28}')
    print(f'Default {"Value":>5}: {test_default}')

    test_custom = Professor("A", "Letter", "L00000000", "N/A")
    print(f'Custom {"Value":>6}: {test_custom}')


def test_property_getters():
    test_get = Professor("A", "Letter", "L00000000", "N/A")

    print(f'{"[Property Getters Test]":-^33}')
    print(f'First Name: {test_get.first_name}, Last Name: {test_get.last_name}, '
          f'L Number: {test_get.l_number}, Department: {test_get.department}')


def test_property_setters():
    test_set = Professor("A", "Letter", "L00000000", "N/A")
    test_set.first_name = "B"
    test_set.last_name = "Letter"
    test_set.l_number = "L00000000"
    test_set.department = "N/A"

    print(f'{"[Property Setters Test]":-^33}')
    print(test_set)


def test_property_setters_with_validation():
    test_set_valid = Professor("A", "Letter", "L00000000", "N/A")

    # try/except first name setter
    try:
        test_set_valid.first_name = 1234567890
    except ValueError as vErr:
        print("an exception was thrown setting first name to a int")
        print(vErr)
    try:
        test_set_valid.first_name = "          "
    except ValueError as vErr:
        print("an exception was thrown setting first name to a empty string")
        print(vErr)

    # try/except last name setter
    try:
        test_set_valid.last_name = 1234567890
    except ValueError as vErr:
        print("an exception was thrown setting last name to a int")
        print(vErr)
    try:
        test_set_valid.last_name = "          "
    except ValueError as vErr:
        print("an exception was thrown setting last name to a empty string")
        print(vErr)

    # try/except l number setter
    try:
        test_set_valid.l_number = 1234567890
    except ValueError as vErr:
        print("an exception was thrown setting l number to a int")
        print(vErr)
    try:
        test_set_valid.l_number = "          "
    except ValueError as vErr:
        print("an exception was thrown setting l number to a empty string")
        print(vErr)

    # try/except l department setter
    try:
        test_set_valid.department = 1234567890
    except ValueError as vErr:
        print("an exception was thrown setting department to a int")
        print(vErr)
    try:
        test_set_valid.department = "          "
    except ValueError as vErr:
        print("an exception was thrown setting department to a empty string")
        print(vErr)


def test_encapsulation():
    test_encap = Professor("A", "Letter", "L0000000", "N/A")
    try:
        user_input = input("TEST ENCAPSULATION WITH ERROR? [Y/N]: ")[0].upper()

        if user_input == "Y":
            print(test_encap.__first_name)
            test_encap.__first_name = "Solo"
            print(test_encap.__first_name)
        else:
            print(test_encap.first_name)
            test_encap.first_name = "Solo"
            print(test_encap.first_name)
    except AttributeError as attErr:
        print("an attribute error was throws in testEncapsultion")
        print(attErr)


def main():
    """ this is main and it runs the program """
    test_constructor()
    print()
    test_property_getters()
    print()
    test_property_setters()
    print()
    test_property_setters_with_validation()
    print()
    test_encapsulation()


if __name__ == '__main__':
    main()
