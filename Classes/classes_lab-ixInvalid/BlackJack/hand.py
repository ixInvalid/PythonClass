from card import *


class Hand:
    """ this class represents a hand of cards """

    def __init__(self):
        """ creates an empty hand """
        self.__cards = []

    @property
    def isEmpty(self):
        """ returns true if the hand is empty """
        return len(self.__cards) == 0

    @property
    def numCards(self):
        """ returns the number of cards in the hand """
        return len(self.__cards)

    def addCard(self, card):
        """ adds a card to the hand """
        self.__cards.append(card)

    def disCard(self, card):
        """ removes a card from the hand """
        self.__cards.remove(card)

    def hasCard(self, card):
        """ returns true if the hand contains the card """
        return card in self.__cards

    def hasCardWithSuit(self, suit):
        """ returns true if the hand contains a card with the given suit """
        for c in self.__cards:
            if c.suit == suit:
                return True
        return False

    def hasCardWithValue(self, value):
        """ returns true if the hand contains a card with the given value """
        for c in self.__cards:
            if c.value == value:
                return True
        return False

    def indexOf(self, card):
        """ returns the index of the card in the hand """
        if card in self.__cards:
            return self.__cards.index(card)
        else:
            return -1

    def __str__(self):
        """ returns a string representation of the hand """
        output = f"Hand["
        for c in self.__cards:
            output += f"{c} "
        output += "]\n"
        return output

    def __getitem__(self, item):
        """ allows a programmer to [] to peek at a card in the hand """
        if isinstance(item, int):
            return self.__cards[item]
        else:
            raise TypeError(f"index must an int {type(item)}  {item}")
