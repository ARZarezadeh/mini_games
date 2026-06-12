def validate_tictactoe_selected_cell(selected_cell, x_cells, o_cells):

    if not selected_cell:
        print("please select a cell...")
        return False
    if len(selected_cell) != 3:
        print("please only enter three character like '1,2'")
        return False

    first_cordinate_number = selected_cell[0]
    seperator = selected_cell[1]
    second_cordinate_number = selected_cell[2]

    if seperator != ',':
        print("seperate two number only with ','")
        return False

    if not first_cordinate_number.isnumeric() or not first_cordinate_number.isnumeric:
        print("only enter integer numbers")
        return False

    if not (1 <= int(first_cordinate_number) <= 3) or not (1 <= int(second_cordinate_number) <= 3):
        print("invalid numbers. numbers should be 1, 2 or 3")
        return False

    listed_selected_cell = convert_selected_cell_to_list(selected_cell)
    if listed_selected_cell in x_cells or listed_selected_cell in o_cells:
        print("this cell selected before...")
        return False
    return True


def convert_selected_cell_to_list(selected_cell):
    """get user_input and turn it to a list

    Args:
        selected_cell (text): user input

    Returns:
        list: converted user input to a list
    """
    return [int(selected_cell[0]), int(selected_cell[-1])]
