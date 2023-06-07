from customer import *


def test_constructor():
    """ this function tests the constructor of a customer object """
    test_default = Customer()

    print(f'{"[Constructor Test]":-^28}')
    print(f'Default {"Value":>5}: {test_default}')

    test_custom = Customer("A", "Letter", "N/A")
    print(f'Custom {"Value":>6}: {test_custom}')


def test_property_getters():
    test_get = Customer("A", "Letter", "N/A")

    print(f'{"[Property Getters Test]":-^33}')
    print(f'First Name: {test_get.first_name}, Last Name: {test_get.last_name}, '
          f'Email: {test_get.email}')


def test_property_setters():
    test_set = Customer("A", "Letter", "N/A")
    test_set.first_name = "B"
    test_set.last_name = "Letter"
    test_set.email = "N/A"

    print(f'{"[Property Setters Test]":-^33}')
    print(test_set)


def test_property_setters_with_validation():
    test_set_valid = Customer("A", "Letter", "N/A")

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
        test_set_valid.email = 1234567890
    except ValueError as vErr:
        print("an exception was thrown setting email to a int")
        print(vErr)
    try:
        test_set_valid.email = "          "
    except ValueError as vErr:
        print("an exception was thrown setting email to a empty string")
        print(vErr)


def test_encapsulation():
    test_encap = Customer("A", "Letter", "N/A")
    try:
        user_input = input("TEST ENCAPSULATION WITH ERROR? [Y/N]: ")[0].upper()

        if user_input == "Y":
            print(test_encap.__first_name)
            test_encap.__first_name = "A"
            print(test_encap.__first_name)
        else:
            print(test_encap.first_name)
            test_encap.first_name = "A"
            print(test_encap.first_name)
    except AttributeError as attErr:
        print("an attribute error was throws in testEncapsulation")
        print(attErr)
