import enum
from domino import *
from random import randint


class Boneyard:
    """ this class represents a 'deck' of dominos """

    def __init__(self, max_dots=6):
        """ creates a list of dominos from 0, 0 up to and including maxDots, maxDots """
        self.__dominos = []
        for i in range(max_dots + 1):
            for j in range(i, max_dots + 1):
                self.__dominos.append(Domino(i, j))

    def shuffle(self):
        """ shuffles the list of dominos """
        for i in range(self.dominosRemaining):
            rnd_index = randint(0, self.dominosRemaining - 1)
            self.__dominos[i], self.__dominos[rnd_index] = self.__dominos[rnd_index], self.__dominos[i]

    @property
    def isEmpty(self):
        """ determines when the list of dominos is empty """
        return len(self.__dominos) == 0

    @property
    def dominosRemaining(self):
        """ returns the number of dominos remaining in the list """
        return len(self.__dominos)

    def draw(self):
        """ returns the 'top' domino in the boneyard + removes the domino from the list """
        if not self.isEmpty:
            d = self.__dominos.pop(0)
            return d
        else:
            return None

    def __getitem__(self, item):
        """ allows a programmer to use [] to peek at a domino in the middle of the boneyard """
        if isinstance(item, int):
            return self.__dominos[item]
        else:
            raise TypeError(f"Index Must Be an Int {type(item)}  {item}")

    def __str__(self):
        """ creates a string representation of the boneyard"""
        output = f'Dominos['
        for index, domino in enumerate(self.__dominos):
            if index in range(6, 28, 6):
                output += '\n' + f'{domino.__str__():>52}'
            else:
                output += domino.__str__()
        output += ']'
        return output
