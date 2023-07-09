# функция, принимающая номер банковской карты и заменяющая первые 12 цифр *
def hide_card(card_number):
    while ' ' in card_number:
        card_number = card_number.replace(' ', '')
    hide_card_number = '*' * 12 + card_number[-4:]
    return hide_card_number


print(hide_card('1034 3948 1944 6327'))
