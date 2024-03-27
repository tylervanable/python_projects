"""
    Print out all of the cards in a deck of cards. Start with printing
    them as if they were numbers.

    Then eventually
    Ace of CLubs
    2 of Clubs....
    King of Hearts

    Tyler
    3/25/24
"""


# Annotate the variables.
suit: int = 0
suit_str: str
card_num: int = 0
card_num_str: str

# Loop through the four suits in a deck of cards.
for suit in range(1,5):
    if suit == 1:
        suit_str = "Clubs"
    elif suit == 2:
        suit_str = "Diamonds"
    elif suit == 3:
        suit_str = "Spades"
    elif suit == 4:
        suit_str = "Hearts"
    # Loop through the thirteen card numbers in a deck of cards.
    for card_num in range(1,14):
        if card_num == 1:
            card_num_str = "Ace"
        elif card_num == 11:
            card_num_str = "Jack"
        elif card_num == 12:
            card_num_str = "Queen"
        elif card_num == 13:
            card_num_str = "King"
        else:
            card_num_str = card_num
        print("{} of {}".format(card_num_str, suit_str))
        card_num += 1
    suit += 1



if card_num == 11:
    card_num_str = "Jack"
if card_num == 12:
    card_num_str = "Queen"
if card_num == 13:
    card_num_str = "King"
