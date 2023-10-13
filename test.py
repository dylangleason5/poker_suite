# Import the functions from your module
from poker_module import check_straight, check_3ofa_kind, check_royal_flush, play_cards

# Test cases for check_straight function
def test_check_straight():
    # Test for a valid straight
    assert check_straight('S5', 'S6', 'S7') == 7
    assert check_straight('S6', 'S5', 'S7') == 7

    # Test for an invalid straight
    assert check_straight('S3', 'SQ', 'SK') == 0

    # Additional test cases
    assert check_straight('SA', 'SK', 'SQ') == 14
    assert check_straight('S2', 'S3', 'S4') == 4

# Test cases for check_3ofa_kind function
def test_check_3ofa_kind():
    # Test for a valid three-of-a-kind
    assert check_3ofa_kind('S9', 'S9', 'S9') == 9
    assert check_3ofa_kind('SK', 'SK', 'SK') == 13

    # Test for an invalid three-of-a-kind
    assert check_3ofa_kind('S2', 'S4', 'S2') == 0
    assert check_3ofa_kind('SA', 'SK', 'SQ') == 0

    # Additional test cases
    assert check_3ofa_kind('S3', 'S3', 'S3') == 3
    assert check_3ofa_kind('S7', 'S7', 'S7') == 7

# Test cases for check_royal_flush function
def test_check_royal_flush():
    # Test for a valid royal flush
    assert check_royal_flush('SA', 'SK', 'SQ') == 14

    # Test for an invalid royal flush
    assert check_royal_flush('S10', 'SJ', 'SK') == 0
    assert check_royal_flush('S9', 'S10', 'SJ') == 0

    # Additional test cases
    assert check_royal_flush('SK', 'SQ', 'SA') == 14
    assert check_royal_flush('SA', 'SK', 'S2') == 0

# Test cases for play_cards function
def test_play_cards():
    # Test for both players having a straight
    assert play_cards('S5', 'S6', 'S7', 'S4', 'S5', 'S6') == 1  # Right wins
    assert play_cards('S9', 'S10', 'SJ', 'S10', 'SJ', 'SQ') == -1  # Left wins
    assert play_cards('S7', 'S8', 'S9', 'SK', 'SA', 'SQ') == 0  # Draw

    # Test for both players having three-of-a-kind
    assert play_cards('SA', 'SK', 'SK', 'SJ', 'SJ', 'SK') == -1  # Left wins
    assert play_cards('S3', 'S3', 'S3', 'S4', 'S4', 'S4') == 1  # Right wins
    assert play_cards('S5', 'S5', 'S5', 'SA', 'SK', 'SQ') == 0  # Draw

    # Test for a mix of hands
    assert play_cards('SA', 'SK', 'SQ', 'S9', 'S10', 'SJ') == -1  # Left wins (royal flush)
    assert play_cards('S7', 'S8', 'S9', 'S9', 'S9', 'SQ') == 1  # Right wins (three-of-a-kind)
    assert play_cards('S2', 'S3', 'S4', 'SK', 'SK', 'SK') == -1  # Left wins (straight)
    assert play_cards('S4', 'S4', 'S4', 'S2', 'S2', 'S3') == 0  # Draw

# Run the test cases
test_check_straight()
test_check_3ofa_kind()
test_check_royal_flush()
test_play_cards()
