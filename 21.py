import random


def create_deck():
    deck = []
    for i in range(2,11):
        for j in ('c','p','b','x'):
            deck.append(str(i)+j)
    for i in ('V','Q','K','T'):
        for j in ('c','p','b','x'):
            deck.append(i+j)
    return deck


def started_hand(deck):
    hand = []
    for i in range(2):
        random.append(random.choice(deck))
        deck.remove(hand[-1])
    return hand,deck 
    


def start_game():
    deck = create_deck()
    hand = []
    hand, deck = started_hand(deck)




start_game()








    


start_game()
        
