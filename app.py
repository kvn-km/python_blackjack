import math
from art import logo
from helpers import deal, able_to_continue, game_loop
print(logo)

dealer = {"name": "dealer", "total": 0, "cards": []}
player = {"name": "player", "total": 0, "cards": []}


def the_game():
    start = input("ENTER to deal.\nSPACE to exit.\n").upper()
    if start == " ":
        exit()
    else:
        deal(player)
        deal(dealer)
        deal(player)
        deal(dealer)

        # print(f"dealer = {dealer}")
        # print(f"player = {player}")

    game_loop(player, dealer, None)


the_game()
