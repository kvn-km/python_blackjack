import random
import math
from art import logo
print(logo)
deck = {
    "A": 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, "J": 4, "Q": 4, "K": 4
}

dealer = {"total": 0}
player = {"total": 0}


def deal(deal_to):
    card = random.choice(list(deck.items()))[0]
    if deck[card] > 0:
        if card in deal_to:
            deal_to[card] += 1
        else:
            deal_to[card] = 1

        deck[card] -= 1

        if card == "J" or card == "Q" or card == "K":
            deal_to["total"] += 10
        elif card == "A":
            if deal_to["total"] >= 11:
                deal_to[f"ace_value{deal_to['A']}"] = 1
                deal_to["total"] += 1
            elif deal_to["total"] <= 10:
                deal_to[f"ace_value{deal_to['A']}"] = 11
                deal_to["total"] += 11
        else:
            deal_to["total"] += card
    else:
        deal(deal_to)


start = input("Deal!\n(or N to cancel)\n").upper()
if start == "N":
    exit()
else:
    deal(dealer)
    deal(player)
    deal(dealer)
    deal(player)


def the_game():
    # 1 deal cards to dealer and player x2
    # 2 check totals
    # 3 if any winners (21), end game
    # 4 if player above 21, end game
    # 5 if player below 21, ask to hit
    # 6 if HIT, deal card to player
    # 7 if dealer below 17, deal card to dealer
    # 8 goto 2
    # 9 end game


print(f"dealer = {dealer}")
print(f"player = {player}")
