def matrix_size() -> tuple[int]:
    col = int(input("please enter a number for col: "))
    row = int(input("please enter a number for row: "))
    return col , row

def find_index():
    num = input("please enter a index: ")
    if len(num)!= 3:
        print("you need enter 2 nums like 2,1")
        num = input("please enter a index")
    index_list = num.split(",")
    return index_list

def print_board(matrix) -> list[list]:
    print(matrix)


# def print_result(matrix:list[list]) -> list[list]:
#     pass


