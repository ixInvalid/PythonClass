from dominoTests import *
from boneyardTests import *


def domino_test():
    """ this runs domino tests """
    testConstructor()
    print()
    testPropertyGetters()
    print()
    testPropertySetters()
    print()
    testPropertySettersWithValidation()
    print()
    testEncapsulation()
    print()
    testIsDouble()
    print()
    testFlip()
    print()
    testEquals()


def boneyard_test():
    """ this runs boneyard tests """
    test_constructor()
    print()
    test_shuffle()
    print()
    test_draw()
    print()
    test_get_item()
    print()
    test_in()
    print()
    test_for_loop()


def main():
    # domino_test()
    boneyard_test()


if __name__ == '__main__':
    main()
