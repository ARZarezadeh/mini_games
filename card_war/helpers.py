from enum import Enum


def insure_get_input(input_message):
    '''
    insure to get the valid input(not empty)
    '''
    valid_name = False
    name = ""
    while not valid_name:
        name = input(f"{input_message}: " or "--- ")
        if name:
            valid_name = True
    return name


class CardNumberMap(Enum):
    '''
    map between name of card numbers
    '''
    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13


def card_number_display(number):
    try:
        return CardNumberMap(number).name
    except ValueError:
        return str(number)
