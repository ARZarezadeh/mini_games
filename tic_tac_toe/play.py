import os
from collections import Counter

from board import Board
from helpers import validate_tictactoe_selected_cell, convert_selected_cell_to_list


class TicTacToe:
    """
    Tic Tac Toe Game
    """

    def __init__(self):
        self.x_cells = []
        self.o_cells = []

    def start_the_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # to clear terminal

        print("game started...")
        board = Board()
        board.show_empty_board()

        x_turn = False
        game_over = False

        while not game_over:
            x_turn = not x_turn
            print(f"{"X" if x_turn else "O"} Turn")
            selected_cell = self.take_user_selected_cell()
            if x_turn:
                self.x_cells.append(selected_cell)
            else:
                self.o_cells.append(selected_cell)
            board.show_the_board(self.x_cells, self.o_cells)
            game_over = self.calculate_winner(self.x_cells, self.o_cells)
        print(f"{"X" if x_turn else "O"} has won !!!")

    def take_user_selected_cell(self):
        """
        take the user input till its valid

        Returns:
            selected_cell (string): user input if its valid
        """
        valid_input = False
        while not valid_input:
            selected_cell = input("select the cell(like 1,2) :")
            valid_input = validate_tictactoe_selected_cell(
                selected_cell, self.x_cells, self.o_cells)
        return convert_selected_cell_to_list(selected_cell)

    def calculate_winner(self, x_cells, o_cells):
        """calculate winner

        Args:
            x_cells (list): _description_
            o_cells (list): _description_

        Returns:
            True: if we have a winner
            False: if no one wins
        """
        x_cells_rows = [lst[0] for lst in x_cells if lst]
        x_cells_columns = [lst[1] for lst in x_cells if lst]
        x_cells_diagonal = [item for item in x_cells if item[0] == item[1]]
        x_cells_anti_diagonal = [
            item for item in x_cells if item[0] + item[1] == 4]
        x_cells_rows_count = Counter(x_cells_rows)
        x_cells_columns_count = Counter(x_cells_columns)
        x_cells_diagonal_count = len(x_cells_diagonal)
        x_cells_anti_diagonal_count = len(x_cells_anti_diagonal)

        o_cells_rows = [lst[0] for lst in o_cells if lst]
        o_cells_columns = [lst[1] for lst in o_cells if lst]
        o_cells_diagonal = [item for item in o_cells if item[0] == item[1]]
        o_cells_anti_diagonal = [
            item for item in o_cells if item[0] + item[1] == 4]
        o_cells_rows_count = Counter(o_cells_rows)
        o_cells_columns_count = Counter(o_cells_columns)
        o_cells_diagonal_count = len(o_cells_diagonal)
        o_cells_anti_diagonal_count = len(o_cells_anti_diagonal)

        if 3 in x_cells_rows_count.values() or 3 in x_cells_columns_count.values() or 3 in o_cells_rows_count.values() or 3 in o_cells_columns_count.values():
            return True
        if x_cells_diagonal_count == 3 or o_cells_diagonal_count == 3:
            return True
        if x_cells_anti_diagonal_count == 3 or o_cells_anti_diagonal_count == 3:
            return True
        return False


def __init__():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start_the_game()


__init__()
