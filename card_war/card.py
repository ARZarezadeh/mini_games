from helpers import CardNumberMap, card_number_display


class Card:
    '''
    class for creating cards of a dec
    '''

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.name = f"{card_number_display(number)} of {suit}"

    def get_name(self):
        return self.name
    
    def get_number(self):
        return self.number
