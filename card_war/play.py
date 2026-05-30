from encodings.punycode import T
import random

from dec import Dec
from Players import Player
from helpers import insure_get_input


player1_name = insure_get_input("what is the name of first player")
player2_name = insure_get_input("what is the name of second player")
player1 = Player(player1_name)
player2 = Player(player2_name)

print(f"Card War : {player1.get_name()} VS {player2.get_name()}")

dec = Dec()
dec.create_dec()
cards = dec.get_cards()
dec.shuffle_cards()


middle_card = len(cards) // 2  # because the number of cards are even
player1_cards = cards[:middle_card]
player2_cards = cards[middle_card:]

already_start = False

while len(player1_cards) and len(player2_cards):
    random.shuffle(player1_cards)
    random.shuffle(player2_cards)
    print(
        f"the number of cards in {player1_name}'s hands: {len(player1_cards)}")
    print(
        f"the number of cards in {player2_name}'s hands: {len(player2_cards)}")
    message = "Next Trun?"
    if not already_start:
        message = "Enter to Start The Game"
        already_start = True
    input(message)
    player1_card = player1_cards.pop(0)
    player2_card = player2_cards.pop(0)
    turn = [player1_card, player2_card]
    this_round_winner_determine = False
    while not this_round_winner_determine:
        print(f"{player1_name} play: {player1_card.get_name()}")
        print(f"{player2_name} play: {player2_card.get_name()}")
        if player1_card.get_number() > player2_card.get_number():
            print(
                f"{player1_name} wins this round. {player1_card.get_name()} is bigger than {player2_card.get_name()}")
            player1_cards.extend(turn)
            this_round_winner_determine = True
        elif player2_card.get_number() > player1_card.get_number():
            print(
                f"{player2_name} wins this round. {player2_card.get_name()} is bigger than {player1_card.get_name()}")
            player2_cards.extend(turn)
            this_round_winner_determine = True
        else:
            print("its a tie. seperate 3 cards and repeat proccess...")
            turn.extend(player1_cards[-3:])
            turn.extend(player2_cards[-3:])
            player1_card = player1_cards.pop(0)
            player2_card = player2_cards.pop(0)
            turn.extend([player1_card, player2_card])
if len(player1_cards):
    print(f"--------- {player1_name} has WON !!!! --------------- ")

elif len(player2_cards):
    print(f"--------- {player2_name} has WON !!!! --------------- ")
