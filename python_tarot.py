from draw import three_card_draw, one_major_draw
from playing_to_tarot import convert_cards


user_input = input("Enter 1 for reading or 2 for card converter: ")

while True:
    if user_input == "1":
        three_card_draw()
        break
    elif user_input == "2":
        convert_cards()
        break
    else:
        user_input = input("Please select 1 or 2 only: ")
