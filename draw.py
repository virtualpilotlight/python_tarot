import random
from card import all_cards, major
from ascii import ascii_past, ascii_present, ascii_future

def three_card_draw():
    draw = random.sample(all_cards, 3)

    past = random.randint(0, 1)
    present = random.randint(0, 1)
    future = random.randint(0, 1)

    print(ascii_past)
    print(draw[0][past])
    print(ascii_present)
    print(draw[1][present])
    print(ascii_future)
    print(draw[2][future])

def one_major_draw():
    one_card = random.sample(major, 1)
    print(one_card)
    print(type(one_card))
    up_or_down = random.randint(0, 1)
    print(up_or_down)
    #print(one_card[up_or_down])
    print(one_card[0])
   # print(one_card[1])
    print(len(one_card))

one_major_draw()
