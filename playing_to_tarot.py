import re
from card_convert import penticles, swords, wands, cups

def convert_cards():
    what_suit = input("What suit? ")
    new_suit = None
    new_number = None
    card_index = None
    face_up_or_down = None

    while new_suit == None:
        if what_suit == "Diamonds":
            new_suit = penticles
        elif what_suit == "Spades":
            new_suit = swords
        elif what_suit == "Clubs":
            new_suit = wands
        elif what_suit == "Hearts":
            new_suit = cups
        else:
            what_suit = input("Please pick a suit; Diamonds, Spades, Clubs, or Hearts: ")

    what_number = input("What number? ")

    while new_number == None:
        if not re.match(r"^(10|[2-9]|[JQKA])$", what_number):
            what_number = input("Please pick a card number; 2-10 or J, Q, K or A: ")
            continue
        if what_number == "Q":
            new_number = new_suit[-1]
        elif what_number == "K":
            new_number = new_suit[-2]
        elif what_number == "J":
            new_number = new_suit[-3]
        elif what_number == "A":
            new_number = new_suit[0]
        else:
            card_number = int(what_number) - 1
            new_number = new_suit[card_number]

    up_or_down = input("Was it facing Up or Down? ")

    while face_up_or_down == None:
        if up_or_down == "Up":
            face_up_or_down = "upright"
            break
        elif up_or_down == "Down":
            face_up_or_down = "inverted"
            break
        else:
            up_or_down = input("Please pick Up or Down: ")

    print(new_number["card number"])
    print(new_number["card name"])
    print(new_number[face_up_or_down])
