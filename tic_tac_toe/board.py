class Board:
    def __init__(self):
        self.matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

    def show_empty_board(self):
        board = "\n"
        for i in range(3):
            board += "⬜️"*3
            board += "\n"

        print(board)

    def show_the_board(self, X_cells, O_cells):
        board = '\n'
        for i in [1, 2, 3]:
            for j in [1, 2, 3]:
                if [i, j] in X_cells:
                    board += '❎'
                elif [i, j] in O_cells:
                    board += '🅾️ '
                else:
                    board += '⬜️'
            board += '\n'

        print(board)
