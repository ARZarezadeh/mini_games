class Board:
    def __init__(self):
        self.matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

    def show_empty_board(self):
        board = ('⬜️' * 3 + '\n') * 3

        print(board)

    def show_the_board(self, x_cells, o_cells):
        board = '\n'
        for i in [1, 2, 3]:
            for j in [1, 2, 3]:
                if [i, j] in x_cells:
                    board += '❎'
                elif [i, j] in o_cells:
                    board += '🅾️ '
                else:
                    board += '⬜️'
            board += '\n'

        print(board)
