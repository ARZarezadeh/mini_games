import os

from board import Board
from helpers import validate_tictactoe_selected_cell
class TicTacToe:
    def __init__(self):
        self.turn_of_x = True
    
    def start_the_game(self):
        os.system('cls' if os.name == 'nt' else 'clear') # to clear terminal
        print("game started...")
        board = Board()
        board.show_empty_board()

        x_turn = True
        x_cells = []
        o_cells = []
        selected_cell = self.take_user_selected_cell()
        print(f"{selected_cell=}")
        selected_cell = self.convert_selected_cell_to_list(selected_cell)
        print(f"{selected_cell=}")
        x_cells.append(selected_cell) if x_turn else o_cells.append(selected_cell)
        board.show_the_board(x_cells,o_cells)

    def take_user_selected_cell(self):
        valid_input = False
        while not valid_input:
            selected_cell = input("select the cell(like 1,2) :")
            valid_input = validate_tictactoe_selected_cell(selected_cell)
        return selected_cell
    
    def convert_selected_cell_to_list(self,selected_cell):
        return [int(selected_cell[0]),int(selected_cell[-1])]



def __init__():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start_the_game()


__init__()