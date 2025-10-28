import random


def create_card(n:int) :
    card = n
    return card

def create_deck(n):
    card_deck = []
    for num in range (1, n ** 2 //2+1):
        card1 = create_card(num)
        card2 = create_card(num)
        card_deck.append(card1)
        card_deck.append(card2)
    return card_deck

def shuffle(deck):
    for _ in range(100):
        index1 = random.randint(1,len(deck)-1)
        index2 = random.randint(1,len(deck)-1)
        if index1 == index2:
            continue
        else:
            deck[index1],deck[index2] = deck[index2],deck[index1]
    return deck

def print_matrix(matrix):
    for col in matrix:
        print(col)

