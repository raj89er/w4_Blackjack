import random
from models import Card, Deck, Player, Dealer

def main():
    # Create a new deck
    new_deck = Deck()
    new_deck.shuffle_deck()

    # Create players
    player1 = Player("Player")
    dealer1 = Dealer()

    while True:
        # Start a new round
        player1.clear_hand()
        dealer1.clear_hand()

        # Deal initial cards
        player1.hit(new_deck.deal_card())
        player1.hit(new_deck.deal_card())
        dealer1.hit(new_deck.deal_card())
        dealer1.hit(new_deck.deal_card())

        # Show initial hands
        print("="*77)
        print(f"\n{player1.name}'s hand:")
        print(player1.hand)
        print(f"Hand total: {player1.hand_value}")
        print("="*77)
        print(f"\nDealer's hand:")
        print(dealer1.show_hand())
        print(f"Hand total: {dealer1.hand_value}") 
        print(f"\nCards left in the deck: {new_deck.cards_left}")

        # Player's turn
        while True:
            print("="*77)
            print(f"\nCards left in the deck: {new_deck.cards_left}")
            print("="*77)
            user_input = input("\nHit or Stand? (h/s): ").lower()
            if user_input == 'h':
                player1.hit(new_deck.deal_card())
                print("="*77)
                print(f"\n{player1.name}'s hand:")
                print(player1.hand)
                print(f"Hand total: {player1.hand_value}")
                if player1.is_bust:
                    print(f"{player1.name} busts! Dealer wins!")
                    break
            elif user_input == 's':
                break
            else:
                print("Invalid choice. Please enter 'h' for Hit or 's' for Stand.")

        # Dealer's turn
        if not player1.is_bust:
            dealer1.turn(new_deck)
            print("="*77)
            print(f"\nDealer's hand:")
            print(dealer1.hand)
            print(f"Hand total: {dealer1.hand_value}")

            # Determine winner
            if dealer1.is_bust or player1.hand_value > dealer1.hand_value:
                print(f"\n{player1.name} wins!")
            elif player1.hand_value < dealer1.hand_value:
                print("\nDealer wins!")
            else:
                print("\nIt's a tie!")

        # Ask if the player wants to play again
        print("="*77)
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again == 'y':
            continue
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
