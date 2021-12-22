"""
File name: blackjack.py
"""
import random

faced_cards = {
    'J' : 10,
    'Q' : 10,
    'K' : 10,
    'A' : 11
}

deck = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
player_hand = []
dealer_hand = []


def calculate_hand(hand):
    subtotal = 0
    for card in hand:
        if card in faced_cards.keys():
            subtotal += faced_cards[card]
        else:
            subtotal += card

    return subtotal


def draw_card(deck, hand):
    card = deck.pop(random.randint(0, len(deck) - 1))
    hand.append(card)


def main():
    for _ in range(2):
        draw_card(deck, player_hand)
    total = calculate_hand(player_hand)
    print(total)
    draw_card(deck, player_hand)
    if total < 11:
        faced_cards['A'] = 1
    total = calculate_hand(player_hand)
    print(total)
    print(deck)


if __name__ == '__main__':
    main()