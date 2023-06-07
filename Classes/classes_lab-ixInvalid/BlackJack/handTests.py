from deck import *
from hand import *
from bjhand import *

# this is a rough run but it works


def main():
    player_wins = 0
    dealer_wins = 0

    while True:
        # create deck and shuffle
        deck = Deck()
        deck.shuffle()

        # create player and dealer hands
        player_hand = BJHand()
        dealer_hand = BJHand()

        # Deal initial cards
        player_hand.addCard(deck.deal())
        dealer_hand.addCard(deck.deal())
        player_hand.addCard(deck.deal())
        dealer_hand.addCard(deck.deal())

        # show initial hands
        print("Player's Hand:", player_hand)
        print("Dealer's Hand:", dealer_hand[0])  # show only the first card of the dealer

        # player's turn
        while True:
            choice = input("Do you want to HIT or STAND? ").upper()
            if choice == "HIT":
                player_hand.addCard(deck.deal())
                print("Player's Hand:", player_hand)
                if player_hand.isBusted():
                    print("Player Busted! Dealer Wins.")
                    dealer_wins += 1
                    break
            elif choice == "STAND":
                break
            else:
                print("Invalid choice! Please choose HIT or STAND.")

        # dealer's turn
        while not player_hand.isBusted():
            if dealer_hand.getScore() < 17:
                dealer_hand.addCard(deck.deal())
                print("Dealer's Hand:", dealer_hand)
                if dealer_hand.isBusted():
                    print("Dealer Busted! Player Wins.")
                    player_wins += 1
                    break
            else:
                break

        # Compare hands and determine the winner
        if not player_hand.isBusted() and not dealer_hand.isBusted():
            if player_hand.getScore() > dealer_hand.getScore():
                print("Player Wins!")
                player_wins += 1
            elif player_hand.getScore() < dealer_hand.getScore():
                print("Dealer Wins!")
                dealer_wins += 1
            else:
                print("It's a Tie!")

        # Show total wins
        print("Player Wins:", player_wins)
        print("Dealer Wins:", dealer_wins)

        # Ask to play again
        play_again = input("Do you want to play again? (Y/N) ").upper()
        if play_again != "Y":
            break


if __name__ == "__main__":
    main()
