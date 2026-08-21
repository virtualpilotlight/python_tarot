import re
import random
from cards import all_cards
from ascii import ascii_past, ascii_present, ascii_future

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
