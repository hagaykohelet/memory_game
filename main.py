from memory.board import create_board, compare_card, reveale_tile, is_won
from memory.game import shuffle,create_deck,create_card,print_matrix
from utills.io import print_board,find_index,matrix_size


def play():

    size = matrix_size()


    visible_matrix,hide_matrix = create_board(int(size[0]),int(size[1]))
    print_matrix(hide_matrix)
    print_matrix(visible_matrix)
    while True:
        i1 = find_index()
        num1,num2 = i1
        tile1 = reveale_tile(visible_matrix,int(num1),int(num2))
        hide_matrix[int(num1)][int(num2)] = tile1
        print_matrix(hide_matrix)

        index2 = find_index()
        num3,num4 = index2
        tile2 = reveale_tile(visible_matrix,int(num3),int(num4))
        hide_matrix[int(num3)][int(num4)] = tile2
        print_matrix(hide_matrix)
        if compare_card(tile1,tile2):
            print("its the same number!")
        else:
            print("its not the same number!")
            hide_matrix[int(num3)][int(num4)] = "x"
            hide_matrix[int(num1)][int(num2)] = "x"
            print_matrix(hide_matrix)
        if is_won(hide_matrix):
            print("victory")
            break

if __name__ == "__main__":
    print(play())