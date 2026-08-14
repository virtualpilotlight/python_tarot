import random
from card import all_cards
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

three_card_draw()
