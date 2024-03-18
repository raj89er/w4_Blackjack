import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def card_val(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return 11
        else:
            return int(self.value)

class Deck:
    def __init__(self):
        self.cards = []  # Initialize the cards list
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
        self.cards_left = len(self.cards)

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards_left == 0:
            print("Out of cards! Game over!")
            return None 

        card = self.cards[self.cards_left - 1]
        self.cards_left -= 1 
        return card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = 0
        self.is_bust = False

    def hit(self, card):
        self.hand.append(card)
        self.calc_hand_val()

    def calc_hand_val(self):
        total_value = 0
        for card in self.hand:
            total_value += card.card_val()
        self.hand_value = total_value
        if self.hand_value > 21:
            self.is_bust = True

    def clear_hand(self):
        self.hand = []
        self.hand_value = 0
        self.is_bust = False

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
        self.show_card1 = False
    
    def show_hand(self):
        if self.show_card1 == True:
            return self.hand
        else:
            return [self.hand[0]]
    
    def turn(self, deck):
        self.show_card1 = True
        while self.hand_value < 17:
            self.hit(deck.deal_card())

class Hand:

    def __init__(self):
        self.cards = []
        self.hand_value = 0
        self.is_bust = False

    def add_card(self, card):
        self.cards.append(card)
        self.calc_hand_val()

    def calc_hand_val(self):
        total_value = 0
        num_aces = 0

        for card in self.cards:
            total_value += card.card_val()
            if card.value == 'A':
                num_aces += 1

        # Adjust Ace value if hand value exceeds 21
        while num_aces > 0 and total_value > 21:
            total_value -= 10
            num_aces -= 1

        self.hand_value = total_value
        self.is_bust = self.hand_value > 21

    def clear_hand(self):
        self.cards = []
        self.hand_value = 0
        self.is_bust = False
