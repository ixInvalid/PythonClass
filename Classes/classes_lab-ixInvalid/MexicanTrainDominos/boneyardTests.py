from boneyard import *
from ANSI.prColor import *

# custom variables to be used throughout the program
boneyard = Boneyard()


def test_constructor():
    """ this function tests the constructor of a customer object """
    print(prRed(f'{"[Testing Constructor]":-^31}'))
    print(f'Except Boneyard of 28 Dominos: {prGreen(boneyard)}')
    print(f'Except {prBlue("dominosRemaining")} Property to be 28 Dominos: {prGreen(boneyard.dominosRemaining)}')
    print(f'Expect {prBlue("isEmpty")} {"Property":>17} to be False: {prGreen(boneyard.isEmpty)}')


def test_shuffle():
    boneyard.shuffle()

    print(prRed(f'{"[Testing Shuffle]":-^27}'))

    print(f'Except Boneyard of 28 Dominos: {prGreen(boneyard)}')
    print(f'Except {prBlue("dominosRemaining")} Property to be 28 Dominos: {prGreen(boneyard.dominosRemaining)}')
    print(f'Expect {prBlue("isEmpty")} {"Property":>17} to be False: {prGreen(boneyard.isEmpty)}')


def test_draw():
    print(prRed(f'{"[Testing Draw]":-^24}'))

    boneyard_ = Boneyard()
    print(f'Except Boneyard of 28 Dominos: {prGreen(boneyard_)}')
    print(f'Except {prBlue("dominosRemaining")} Property to be 28 Dominos: {prGreen(boneyard_.dominosRemaining)}')
    print(f'Expect {prBlue("isEmpty")} {"Property":>17} to be False: {prGreen(boneyard_.isEmpty)}')

    domino = boneyard_.draw()
    print(f'After Call to {prBlue("Draw")}...')
    print(f'Except Boneyard of 27 Dominos: {prGreen(boneyard_)}')
    print(f'Except {prBlue("dominosRemaining")} Property to be 27 Dominos: {prGreen(boneyard_.dominosRemaining)}')
    print(f'Expect {prBlue("isEmpty")} {"Property":>17} to be False: {prGreen(boneyard_.isEmpty)}')
    print(f"Expect Drawn Domino to be Domino(0 | 0): {domino}")

    for i in range(boneyard_.dominosRemaining):
        domino = boneyard_.draw()
    print(f"Drawn the Remaining Cards... Expect Empty Boneyard: {prGreen(boneyard_)}")
    print(f'Except {prBlue("dominosRemaining")} Property to be 0 Dominos: {prGreen(boneyard_.dominosRemaining)}')
    print(f'Expect {prBlue("isEmpty")} {"Property":>17} to be True: {prGreen(boneyard_.isEmpty)}')


def test_get_item():
    print(prRed(f'{"[Testing Get Item]":-^28}'))

    print(f'Except Boneyard of 28 Dominos: {prGreen(boneyard)}')
    print(f'Except {prBlue("dominosRemaining")} Property to be 28 Dominos: {prGreen(boneyard.dominosRemaining)}')
    print(f'Expect {prBlue("isEmpty")} {"Property":>17} to be False: {prGreen(boneyard.isEmpty)}')

    domino = boneyard[27]
    print(f'Used [28]...')
    print(f'Except Boneyard of 28 Dominos. {prGreen(boneyard)}')
    print(f'Except {prBlue("dominosRemaining")} Property to be 28 Dominos: {prGreen(boneyard.dominosRemaining)}')
    print(f'Expect {prBlue("isEmpty")} {"Property":>17} to be False: {prGreen(boneyard.isEmpty)}')
    print(f"Expect Last Domino to be Domino(1 | 2): {prGreen(domino)})")


def test_in():
    boneyard_ = Boneyard()
    domino_a = boneyard_.draw()

    print(prRed(f'{"[Testing In]":-^22}'))

    print(f"Current UnShuffled Boneyard without Domino(0 | 0): {prGreen(boneyard_)}")
    domino_b = boneyard_[-1]
    print(f"is Domino(0 | 0) in the Boneyard?  Expect False:  {prGreen(domino_a in boneyard_)}")
    print(f"is Domino(6 | 6) in the Boneyard?  Expect True:   {prGreen(domino_b in boneyard_)}")


def test_for_loop():
    print(prRed(f'{"[Testing For Loop]":-^28}'))
    print(f'Iterating Through the Boneyard with {prBlue("For In")}...  Expect 28 Individual Dominos:')
    for domino in boneyard:
        print(prGreen(domino))
