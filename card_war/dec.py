import random
from card import Card


class Dec:
    def __init__(self):
        self.cards = []

    def create_dec(self):
        '''
        return all cards in the dec
        '''
        numbers = [1, 2, 3,4]
        suits = ['heart']
        for number in numbers:
            for suit in suits:
                card = Card(number, suit)
                self.cards.append(card)

    def get_cards(self):
        '''
        get method for cards
        '''
        if len(self.cards) == 0:
            raise Exception(
                "there is no cards in this dec yet. call 'create_dec' method first.")
        return self.cards

    def shuffle_cards(self):
        '''
        shuffle the cards
        '''
        if len(self.cards) == 0:
            raise Exception(
                "there is no cards in this dec yet. call 'create_dec' method first.")
        random.shuffle(self.cards)
