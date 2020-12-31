import math
from art import logo
from helpers import deal, able_to_continue, game_loop
print(logo)

dealer = {"name": "dealer", "total": 0, "cards": []}
player = {"name": "player", "total": 0, "cards": []}


def the_game():
    # 1 deal cards to dealer and player x2
    start = input("ENTER to deal.\nSPACE to exit.\n").upper()
    if start == " ":
        exit()
    else:
        deal(player)
        deal(dealer)
        deal(player)
        deal(dealer)

        print(f"dealer = {dealer}")
        print(f"player = {player}")

    # 2 check totals
    # 3 if any winners (21), end game
    # 4 if player above 21, end game

    game_loop(player, dealer)

    # 5 if player below 21, ask to hit
    # 6 if HIT, deal card to player
    # 7 if dealer below 17, deal card to dealer
    # 8 goto 2
    # 9 end game


the_game()
