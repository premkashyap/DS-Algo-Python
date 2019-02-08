from random import shuffle
from enum import Enum

suits = ["Heart", "Diamond", "Spade", "Club"]
values = {'Ace':11, 'Two':2, 'Three':3, 'Four':4, 'Five':5 ,'Six':6, 'Seven': 7, 'Eight':8, 'Nine':9, 'Ten': 10, 'Joker': 10, 'Queen':10, 'King': 10}



class Card():
    def __init__(self, suit, face_value):
        self.suit = suit
        self.face_value = face_value

    def __str__(self):
        return '{} of {}'.format(self.face_value, self.suit,)

    def get_points(self):
        return values[self.face_value]

class Deck():
    def __init__(self, number_of_packs):
        self.pack = [Card(suit, face_value) for suit in suits for face_value in values for i in range(number_of_packs)]

    def print_pack(self):
        for card in self.pack:
            print(str(card))

    def shuffle(self):
        shuffle(self.pack)

    def pop(self):
        return (self.pack.pop(), self.pack.pop())
    
    def get_cards(self):
        return self.pack
            
class Player():
    def __init__(self, name):
        self.name = name
        self.hands = []

    def get_points(self):
        points = 0
        for card in self.hands:
            points+=card.get_points()
        return points

    def add_hands(self, hand):
        self.hands.append(hand)
    
    def remove_hands(self, hand):
        self.hands.remove(hand)
        
    def get_hands(self):
        return self.hands

class Dealer():
    def __init__(self):
        self.hands = []

    def get_total_score(self):
        points = 0
        for card in self.hands:
            points+=card.get_points()
        return points

class Shoe():
    def __init__(self, no_of_decks):
        self.no_of_decks = no_of_decks
        self.create_shoe()

    def create_shoe(self):
        self.cards = [card for deck in self.no_of_decks for card in deck.get_cards()]
        self.shuffle()
    
    def shuffle(self):
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    

class Game():
    def __init__(self, player, dealer, no_of_decks):
        self.player = player
        self.dealer = dealer
        



    


if __name__ == '__main__':
    pack = Pack(2)
    pack.shuffle()
    pack.print_pack()