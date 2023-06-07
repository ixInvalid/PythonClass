from hand import *


class BJHand(Hand):
    """This class represents a hand of cards for BJ"""
    def __init__(self):
        """Creates an empty hand"""
        super().__init__()

    def hasAce(self):
        """Returns True if the hand contains an Ace"""
        for c in self._Hand__cards:
            if c.value == 1:
                return True
        return False

    def isBusted(self):
        """Returns True if the hand is busted"""
        return self.getScore() > 21

    def getScore(self):
        score = 0
        num_aces = 0

        for card in self._Hand__cards:
            if card.value == 1:  # Ace
                num_aces += 1
                score += 11  # Treat the first Ace as 11 initially
            elif card.value in range(2, 11):  # Number cards
                score += card.value
            else:
                score += 10  # Face cards

        # Adjust the value of Aces if the score exceeds 21
        while score > 21 and num_aces > 0:
            score -= 10  # Convert one Ace from 11 to 1
            num_aces -= 1

        return score