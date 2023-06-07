import deckTests as d
import cardTests as c
import bjhand as bj


def deck_test():
    d.testConstructor()
    print()
    d.testShuffle()
    print()
    d.testDeal()
    print()
    d.testGetItem()
    print()
    d.testIn()
    print()
    d.testForLoop()


def card_test():
    c.test_constructor()
    print()
    c.test_property_getters()
    print()
    c.test_property_setters()
    print()
    c.test_property_setters_with_validation()
    print()
    c.test_encapsulation()
    print()
    c.test_has_matching_suit()
    print()
    c.test_has_matching_value()
    print()
    c.test_is_club()
    print()
    c.test_is_diamond()
    print()
    c.test_is_heart()
    print()
    c.test_is_spade()
    print()
    c.test_is_black()
    print()
    c.test_is_red()
    print()
    c.test_is_face_card()


def main():
    """ this is main and it runs the program """
    # deck_test()
    # card_test()


if __name__ == '__main__':
    main()
