class Card:
    """ This class represents a playing card.
        A card has 2 attributes, value and suit.  value is an int between 1 and 13.  suit is an int between 1 and 4.
        It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""
    # these lists are used in __str__
    # they are class variables rather than instance variables and are shared by each object of the class
    __suits = ["", "Clubs", "Diamonds", "Hearts", "Spades"]
    __values = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Ten", "Jack", "Queen", "King"]

    def __init__(self, suit=0, value=0):
        self.__suit = suit
        self.__value = value

    @property
    def suit(self):
        # return Card.__suits[self.__suit]
        return self.__suit

    @property
    def value(self):
        # return Card.__values[self.__value]
        return self.__value

    @suit.setter
    def suit(self, suit):
        if isinstance(suit, int) and 0 <= suit <= 4:
            self.__suit = suit
        else:
            raise ValueError(f"suit must an integer between 0 and 4 {type(suit)}  {suit}")

    @value.setter
    def value(self, value):
        if isinstance(value, int) and 0 <= value <= 13:
            self.__value = value
        else:
            raise ValueError(f"value must an integer between 0 and 4 {type(value)}  {value}")

    def hasMatchingSuit(self, other):
        if self.__suit == other.suit:
            return True
        else:
            return False

    def hasMatchingValue(self, other):
        if self.__value == other.value:
            return True
        else:
            return False

    def isClub(self):
        if self.__suit == 1:
            return True
        else:
            return False

    def isDiamond(self):
        if self.__suit == 2:
            return True
        else:
            return False

    def isHeart(self):
        if self.__suit == 3:
            return True
        else:
            return False

    def isSpade(self):
        if self.__suit == 4:
            return True
        else:
            return False

    def isBlack(self):
        if self.__suit == 1 or 4:
            return True
        else:
            return False

    def isRed(self):
        if self.__suit == 2 or 3:
            return True
        else:
            return False

    # def isFaceCard(self):
    #     if self.__value == "Jack" or "Queen" or "King":
    #         return True
    #     else:
    #         return False

    def isFaceCard(self):
        for i in range(11, 14):
            if self.__value == i:
                return True
        else:
            return False

    def __str__(self):
        return f'Card: {Card.__values[self.__value]} of {Card.__suits[self.__suit]}'

    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 cards.  if card1 == card2 for example.
            2 cards are equal if they're both cards and if their attributes have the same values"""
        if isinstance(other, Card):
            return self.__suit == other.suit and self.__value == other.value
        else:
            return False
