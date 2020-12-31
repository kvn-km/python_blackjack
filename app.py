import math
from art import logo
from helpers import deal, able_to_continue
print(logo)

dealer = {"name": "dealer", "total": 0}
player = {"name": "player", "total": 0}


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

    # 2 check totals
    # 3 if any winners (21), end game
    # 4 if player above 21, end game
    def game_loop():
        if able_to_continue(player) is True:
            ask_to_hit = input("ENTER to hit.\nSPACE to stay.\n")
            if ask_to_hit == "":
                deal(player)
                if able_to_continue(dealer) is true:
                    deal(dealer)
                game_loop()
            elif ask_to_hit == " ":
                if able_to_continue(dealer) is true:
                    deal(dealer)
                else:
                    print("Both sides stay.")

    # 5 if player below 21, ask to hit
    # 6 if HIT, deal card to player
    # 7 if dealer below 17, deal card to dealer
    # 8 goto 2
    # 9 end game


the_game()

print(f"dealer = {dealer}")
print(f"player = {player}")
