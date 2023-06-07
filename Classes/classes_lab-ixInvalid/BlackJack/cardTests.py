from card import *


def test_constructor():
    test_default = Card()

    print(f'{"[Constructor Test]":-^28}')
    print(f'Default Value: {test_default}')

    test_custom = Card(3, 9)
    print(f'Custom Value: {test_custom}')


def test_property_getters():
    test_get = Card(3, 9)
    print("TESTING PROPERTY GETTERS")
    print(f"SUIT: {test_get.suit}, VALUE: {test_get.value}")


def test_property_setters():
    test_set = Card(3, 9)
    test_set.suit = 4
    test_set.value = 1
    print(f"TESTING PROPERTY GETTERS\n{test_set}")


def test_property_setters_with_validation():
    test_set_valid = Card(3, 9)

    # try/except suit setter
    try:
        test_set_valid.suit = "Heart"
    except ValueError as vErr:
        print("an exception was thrown setting suit to a string")
        print(vErr)
    try:
        test_set_valid.suit = -1
    except ValueError as vErr:
        print("an exception was thrown setting suit to -1")
        print(vErr)

    # try/except value setter
    try:
        test_set_valid.value = "Ace"
    except ValueError as vErr:
        print("an exception was thrown setting value to a string")
        print(vErr)
    try:
        test_set_valid.value = -1
    except ValueError as vErr:
        print("an exception was thrown setting value to -1")
        print(vErr)


def test_encapsulation():
    test_encap = Card(3, 9)
    try:
        user_input = input("TEST ENCAPSULATION WITH ERROR? [Y/N]: ")[0].upper()

        if user_input == "Y":
            print(test_encap.__suit)
            test_encap.suit = 4
            print(test_encap.__suit)
        elif user_input == "N":
            print(test_encap.suit)
            test_encap.suit = 4
            print(test_encap.suit)
        else:
            print("WRONG INPUT")
    except AttributeError as attErr:
        print("an attribute error was throws in testEncapsultion")
        print(attErr)


def test_has_matching_suit():
    test_card = Card(3, 9)
    test_other_card = Card(3, 1)

    print(f"TESTING hasMathingSuit...  SHOULD RETURN TRUE ({test_card} | {test_other_card}): "
          f"{test_card.hasMatchingSuit(test_other_card)}")


def test_has_matching_value():
    test_card = Card(2, 9)
    test_other_card = Card(3, 9)

    print(f"TESTING hasMathingValue... SHOULD RETURN TRUE ({test_card} | {test_other_card}): "
          f"{test_card.hasMatchingValue(test_other_card)}")


def test_is_club():
    test_card = Card(1, 9)

    print(f"TESTING isClub... SHOULD BE CLUB: {test_card.isClub()}")


def test_is_diamond():
    test_card = Card(2, 9)

    print(f"TESTING isDiamond... SHOULD BE CLUB: {test_card.isDiamond()}")


def test_is_heart():
    test_card = Card(3, 9)

    print(f"TESTING isHeart... SHOULD BE HEART: {test_card.isHeart()}")


def test_is_spade():
    test_card = Card(4, 9)

    print(f"TESTING isSpade... SHOULD BE SPADE: {test_card.isSpade()}")


def test_is_black():
    test_card = Card(1, 9)

    print(print(f"TESTING isBlack... SHOULD BE BLACK ({test_card}): {test_card.isBlack()}"))


def test_is_red():
    test_card = Card(2, 9)

    print(print(f"TESTING isRed... SHOULD BE RED ({test_card}): {test_card.isRed()}"))


def test_is_face_card():
    test_card = Card(3, 1)

    print(print(f"TESTING isFaceCard... SHOULD BE A FACE CARD ({test_card}): {test_card.isFaceCard()}"))
