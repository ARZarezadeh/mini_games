def validate_tictactoe_selected_cell(selected_cell):
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

    if not first_cordinate_number.isnumeric() or  not first_cordinate_number.isnumeric:
        print("only enter integer numbers")
        return False

    if not (1<=int(first_cordinate_number) <=3) or not (1<=int(second_cordinate_number) <=3):
        print("invalid numbers. numbers should be 1, 2 or 3")
        return False

    return True