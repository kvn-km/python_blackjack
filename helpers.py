import random

deck = {
    "A": 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, "J": 4, "Q": 4, "K": 4
}


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
                for key in deal_to:
                    if "ace_value" in key and deal_to[key] == 11:
                        deal_to[key] = 1
                        deal_to["total"] -= 10
                    else:
                        deal_to[f"ace_value{deal_to['A']}"] += 1
                        deal_to["total"] += 11

                        else:

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
            print(":( YOU LOSE! Player busts!")
            exit()
        elif check_for["name"] == "dealer":
            print(":) YOU WIN! Dealer busts!")
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
