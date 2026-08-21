import random
#from card import all_cards, major
from ascii import ascii_past, ascii_present, ascii_future
from card_convert import new_cards, major

def three_card_draw():
    draw = random.sample(new_cards, 3)

    past = random.randint(0, 1)
    present = random.randint(0, 1)
    future = random.randint(0, 1)

    print(ascii_past)
    print(draw[0]["card name"])
    print(draw[0]["card number"])
    if past == 0:
        print(f"upright: {draw[0]["upright"]}")
    else:
        print(f"inverted: {draw[0]["inverted"]}")
    print(ascii_present)
    print(draw[1]["card name"])
    print(draw[1]["card number"])
    if present == 0:
        print(f"upright: {draw[1]["upright"]}")
    else:
        print(f"inverted: {draw[1]["inverted"]}")
    print(ascii_future)
    print(draw[2]["card name"])
    print(draw[2]["card number"])
    if future == 0:
        print(f"upright: {draw[2]["upright"]}")
    else:
        print(f"inverted: {draw[2]["inverted"]}")

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

#one_major_draw()
