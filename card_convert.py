import re
from cards import all_cards

def parse_card_line(line):
    m = re.match(r"^(\|.+?\|)\s*-\s*(.+?)\s*-\s*(upright|inverted)\s*-\s*(.+)$", line.strip())
    card_number, card_name, orientation, meaning = m.groups()
    return card_number, card_name, orientation, meaning

def convert(all_cards):
    result = []
    for upright_line, inverted_line in all_cards:
        num, name, _, upright_meaning = parse_card_line(upright_line)
        _, _, _, inverted_meaning = parse_card_line(inverted_line)
        result.append({
            "card number": num,
            "card name": name,
            "upright": upright_meaning,
            "inverted": inverted_meaning,
        })
    return result

new_cards = convert(all_cards)


major = new_cards[0:22]

penticles = new_cards[22:36]
swords = new_cards[36:50]
wands = new_cards[50:64]
cups = new_cards[64:]
