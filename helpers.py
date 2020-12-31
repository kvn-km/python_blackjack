import random

deck = {
    "A": 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, "J": 4, "Q": 4, "K": 4
}


def reduce_value_of_an_ace(deal_to):
    status = False
    for key in list(deal_to.keys()):
        if type(key) != int and key.find("ace_value") == 0 and deal_to[key] == 11:
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


def check_for_winners(check_for, player, dealer):
    if check_for["total"] == 21:
        if check_for["name"] == "player":
            print("")
            print("------END GAME------")
            print(f"DEALER SHOWS : {' '.join(dealer['cards'])}")
            print(f"PLAYER SHOWS : {' '.join(player['cards'])}")
            print(":) YOU WIN! Player wins with Blackjack!\n")
            exit()
        elif check_for["name"] == "dealer":
            print("")
            print("------END GAME------")
            print(f"DEALER SHOWS : {' '.join(dealer['cards'])}")
            print(f"PLAYER SHOWS : {' '.join(player['cards'])}")
            print(":( YOU LOSE! Dealer wins with Blackjack!\n")
            exit()


def check_for_busts(check_for, player, dealer):
    if check_for["total"] > 21:
        print("check for " + check_for["name"])
        if reduce_value_of_an_ace(check_for) is True:
            print("check for " + check_for["name"] + " REDUCE.")
            check_for_busts(check_for, player, dealer)
        else:
            if check_for["name"] == "player":
                print("")
                print("------END GAME------")
                print(f"DEALER SHOWS : {' '.join(dealer['cards'])}")
                print(f"PLAYER SHOWS : {' '.join(player['cards'])}")
                print(
                    f":( YOU LOSE! Player busts with {check_for['total']}. Dealer holds {dealer['total']}.\n")
                exit()
            elif check_for["name"] == "dealer":
                print("")
                print("------END GAME------")
                print(f"DEALER SHOWS : {' '.join(dealer['cards'])}")
                print(f"PLAYER SHOWS : {' '.join(player['cards'])}")
                print(
                    f":) YOU WIN! Dealer busts with {check_for['total']}. Player holds {player['total']}.\n")
                exit()


def able_to_continue(check_for, player, dealer):
    check_for_winners(check_for, player, dealer)
    check_for_busts(check_for, player, dealer)
    if check_for["name"] == "player":
        return True
    elif check_for["name"] == "dealer":
        if check_for["total"] >= 17:
            return False
        else:
            return True


def game_loop(player, dealer, hit_or_stay):
    # print("--------------------")
    # print(f"dealer = {dealer}")
    # print(f"player = {player}")
    # print("--------------------")
    print("--------------------")
    print(f"DEALER SHOWS : {list(dealer.keys())[3]}")
    print(f"PLAYER SHOWS : {' '.join(player['cards'])}")
    if able_to_continue(player, player, dealer) is True:
        if hit_or_stay == None:
            ask_to_hit = input("ENTER to hit.\nSPACE to stay.\n")
            if ask_to_hit == "":
                print("HIT")
                deal(player)
                game_loop(player, dealer, None)
            elif ask_to_hit == " ":
                print("STAY")
                game_loop(player, dealer, "stay")
        elif hit_or_stay == "stay":
            if able_to_continue(dealer, player, dealer) is True:
                deal(dealer)
                game_loop(player, dealer, "stay")
            else:
                print("------END GAME------")
                print(f"DEALER SHOWS : {' '.join(dealer['cards'])}")
                print(f"PLAYER SHOWS : {' '.join(player['cards'])}")
                player = player["total"]
                dealer = dealer["total"]
                if player > dealer:
                    print(":) YOU WIN! Player wins with " + str(player) +
                          ". Dealer holds " + str(dealer) + ".\n")
                elif dealer > player:
                    print(":( YOU LOSE! Dealer wins with " +
                          str(dealer) + ". Player holds " + str(player) + ".\n")
                elif player == dealer:
                    print(":| DRAW! It's a tie with " +
                          str(player) + ":" + str(dealer) + ".\n")
