import random

from memory.game import create_deck, shuffle




def create_board(n1, n2):
    card = shuffle(create_deck(n1))
    hide_matrix = []
    visible_matrix = []
    index=0
    for col in range(n1):
        hide_line = []
        visible_line = []
        for row in range(n2):
            hide_line.append(card[index])
            visible_line.append("x")
            index+=1
        hide_matrix.append(hide_line)
        visible_matrix.append(visible_line)
    return hide_matrix,visible_matrix


def reveale_tile(board, x ,y):
    return board[x][y]




def compare_card(c1:int ,c2:int) -> bool:
    if c1 == c2:
        return True
    else:
        return False


def is_won(matrix):
    for row in matrix:
        for j in row:
            if j == "x":
                return False

    return True



