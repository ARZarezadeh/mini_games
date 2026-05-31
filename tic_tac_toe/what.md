# TIC_TAC_TOE
## how to play
- two player game
- play on a 3x3 grid
- players alternate marking the cells with X and O
- first player who align 3 of their marks in a row wins(horizontally,vertically,diagonally)


## tachnical
- board(two dimensional array)
    -represent with: | __ X O
- turn(alternate)
- logic of win
    - horizontal: the first location number of three marks are the same
    - vertical: the second location number of three marks are the same
    - diagonal: ((1,1),(2,2),(3,3)) or ((1,3), (2,2),(3,1))