import random


def create_board(n1:int, n2:int) -> list[list[str]]:
    hide_matrix = []
    visible_matrix = []
    for col in range(n1):
        hide_line = []
        visible_line = []
        for row in range(n1):
            hide_line.append("X")
            visible_line.append(n1)
        hide_matrix.append(hide_line)
        visible_matrix.append(visible_line)
    return hide_matrix,visible_matrix



def create_card(n:int) :
    card = n
    return card

def create_deck(n):
    card_deck = []
    for num in range (n):
        card1 = create_card(num)
        card2 = create_card(num)
        card_deck.append(card1)
        card_deck.append(card2)
    return card_deck



def compare_card(c1:int ,c2:int) -> bool:
    if c1 == c2:
        return True
    else:
        return False




def shuffle(deck:list[dict]):
    for _ in range(100):
        index1 = random.randint(0,len(deck)-1)
        index2 = random.randint(0,len(deck)-1)
        if index1 == index2:
            continue
        else:
            deck[index1],deck[index2] = deck[index2],deck[index1]
    return deck



