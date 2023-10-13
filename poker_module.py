# strip cards to int value
def card_value(card):
    if card == 'SJ':
        return 11
    elif card == 'SQ':
        return 12
    elif card == 'SK':
        return 13
    elif card == 'SA':
        return 14
    else:
        return int(card[1:])


# checks if hand is a straight
def check_straight(card1, card2, card3):
    card_nums = []

    for card in card1, card2, card3:
        num = card_value(card)
        card_nums.append(num)

    sorted_cards = sorted(card_nums)

    if sorted_cards[-1] - sorted_cards[1] == sorted_cards[1] - sorted_cards[0] == 1:
        return sorted_cards[-1]
    else:
        return 0


# checks if hand is 3 of a kind
def check_3ofa_kind(card1, card2, card3):
    card_nums = []

    for card in card1, card2, card3:
        num = card_value(card)
        card_nums.append(num)

    if card_nums[0] == card_nums[1] == card_nums[2]:
        return card_nums[0]
    else:
        return 0


# checks if hand is a royal flush
def check_royal_flush(card1, card2, card3):
    card_nums = []

    for card in card1, card2, card3:
        num = card_value(card)
        card_nums.append(num)

    sorted_cards = sorted(card_nums)

    if sorted_cards[-1] - sorted_cards[1] == sorted_cards[1] - sorted_cards[0] == 1 and sorted_cards[-1] == 14:
        return 14
    else:
        return 0


# plays a round of poker
def play_cards(left1, left2, left3, right1, right2, right3):
    # split cards into left and right groups
    left_hand = left1, left2, left3
    right_hand = right1, right2, right3

    # all exact ties immediately result in a draw
    if left_hand == right_hand:
        return 0

    # if not a draw, check for who has a royal flush to win
    left_royal = check_royal_flush(left1, left2, left3)
    right_royal = check_royal_flush(right1, right2, right3)

    if left_royal == 14:
        return -1
    elif right_royal == 14:
        return 1

    # if not a draw and no royal flushes, check for who has a straight to win
    left_straight = check_straight(left1, left2, left3)
    right_straight = check_straight(right1, right2, right3)

    if left_straight != 0 and right_straight == 0:
        return -1

    elif left_straight == 0 and right_straight != 0:
        return 1

    # if not a draw and no royal flushes and no straights, check for the highest 3 of a kind to win
    left_3 = check_3ofa_kind(left1, left2, left3)
    right_3 = check_3ofa_kind(right1, right2, right3)

    if left_3 > right_3:
        return -1
    elif left_3 < right_3:
        return 1

    else:
        return 0

# Entry point for your code (you can add your main code here)
if __name__ == '__main__':
    print('This is not meant to be run as the main program.')