from card_convert import penticles, swords, wands, cups

what_suit = input("What suit? ")
new_suit = None
new_number = None
card_index = None

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

while  new_number == None:
    if what_number == "Q":
        new_number = new_suit[-1]
    elif what_number == "K":
        new_number = new_suit[-2]
    elif what_number == "J":
        new_number = new_suit[-3]
    elif what_number == "A":
        new_number = new_suit[0]
    elif (int(what_number) >= 2) and (int(what_number) <= 10):
        card_number = int(what_number) - 1
        new_number = new_suit[card_number]
    else:
        what_number = input("Please pick a card number; 2-10 or J, Q, K or A: ")
