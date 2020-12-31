import random

deck = {
    "A": 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, "J": 4, "Q": 4, "K": 4
}


def reduce_value_of_an_ace(deal_to):
    status = False
    for key in deal_to:
        if "ace_value" in key and deal_to[key] == 11:
            deal_to[key] = 1
            deal_to["total"] -= 10
            status = True
            break
    return status


def try_values_for_ace(deal_to):
    if deal_to["total"] >= 11:
        if reduce_value_of_an_ace(deal_to) is True:
            try_values_for_ace(deal_to)
        else:
            deal_to["total"] += 1
            deal_to[f"ace_value{deal_to['A']}"] = 1
    else:
        deal_to["total"] += 11
        deal_to[f"ace_value{deal_to['A']}"] = 11


def deal(deal_to):
    card = random.choice(list(deck.items()))[0]
    if deck[card] > 0:
        if card in deal_to:
            deal_to[card] += 1
            deal_to["cards"].append(str(card))
        else:
            deal_to[card] = 1
            deal_to["cards"].append(str(card))

        deck[card] -= 1

        if card == "J" or card == "Q" or card == "K":
            deal_to["total"] += 10
        elif card == "A":
            try_values_for_ace(deal_to)
        else:
            deal_to["total"] += card
    else:
        deal(deal_to)


def check_for_winners(check_for):
    if check_for["total"] == 21:
        if check_for["name"] == "player":
            print(":) YOU WIN! Player wins with Blackjack!")
            exit()
        elif check_for["name"] == "dealer":
            print(":( YOU LOSE! Dealer wins with Blackjack!")
            exit()


def check_for_busts(check_for):
    if check_for["total"] > 21:
        if check_for["name"] == "player":
            print(f":( YOU LOSE! Player busts with {check_for['total']}!")
            exit()
        elif check_for["name"] == "dealer":
            print(f":) YOU WIN! Dealer busts with {check_for['total']}!")
            exit()


def able_to_continue(check_for):
    check_for_winners(check_for)
    check_for_busts(check_for)
    if check_for["name"] == "player":
        return True
    elif check_for["name"] == "dealer":
        if check_for["total"] >= 17:
            return False
        else:
            return True


def game_loop(player, dealer):
    print(f"DEALER SHOWS : {list(dealer.keys())[3]}")
    print(f"PLAYER SHOWS : {' '.join(player['cards'])}")
    print("\n")
    if able_to_continue(player) is True:
        ask_to_hit = input("ENTER to hit.\nSPACE to stay.\n")
        if ask_to_hit == "":
            deal(player)
            if able_to_continue(dealer) is True:
                deal(dealer)
            game_loop(player, dealer)
        elif ask_to_hit == " ":
            if able_to_continue(dealer) is True:
                deal(dealer)
            else:
                print("Both sides stay.")
