from random import shuffle, choice

def shuffle_deck(deck):
    shuffle(deck)

def dist_cards(deck, player, bot_1, bot_2, bot_3):
    for i in range(13):
        player['hand'].append(deck.pop())
        bot_1['hand'].append(deck.pop())
        bot_2['hand'].append(deck.pop())
        bot_3['hand'].append(deck.pop())

def print_board(floor):
    sort_cards_as_ref_list(floor)
    for i in ['s', 'd', 'h', 'c']:
        if len(floor[i]) < 2:
            print(floor[i])
        else:
            print(floor[i][0], floor[i][-1])
        
        

def sorted_list(card):
    ref_list = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
    return ref_list.index(card[1:])

def sort_cards_as_ref_list(floor):
    for i in ['s', 'd', 'h', 'c']:
        floor[i].sort(key=sorted_list)

def game_is_running(player, bot_1, bot_2, bot_3):
    """returns False when Number of people with no cards more than 2,
    otherwise return True"""

    num_ppl_with_no_cards = 0
    if len(player['hand']) == 0:
        num_ppl_with_no_cards += 1
    if len(bot_1['hand']) == 0:
        num_ppl_with_no_cards += 1
    if len(bot_2['hand']) == 0:
        num_ppl_with_no_cards += 1
    if len(bot_3['hand']) == 0:
        num_ppl_with_no_cards += 1

    if num_ppl_with_no_cards > 2:
        return False
    else:
        return True
    
def print_scores(player, bot_1, bot_2, bot_3):
    print()
    print("Player is: ", player["place"])
    print("BOT_1 is: ", bot_1["place"])
    print("BOT_2 is: ", bot_2["place"])
    print("BOT_3 is: ", bot_3["place"])



def playable_cards(player, floor):
    """ case1: No cards on a specific suit
        case2: there's only the J of the suit
        case3: there's two or more cards in the suit"""
    list_of_playable_cards = []
    mincard = None
    maxcard = None
    #-------check_for_all_possible_playable_cards------#
    for i in ['s', 'd', 'h', 'c']:
        if floor[i] == []:
            list_of_playable_cards.append(i+'J')
        if floor[i] == [i+'J']:
            list_of_playable_cards.append(i+'10')
            list_of_playable_cards.append(i+'Q')
        if len(floor[i]) > 1:
            #------Find_Playable_Cards_Above_J-------#
            if floor[i][0][1] == "J":
                maxcard = i+"Q"
            elif floor[i][0][1] == "Q":
                maxcard = i+"K"
            elif floor[i][0][1] == "K":
                maxcard = i+"A"
            #------Find_Playable_Cards_Below_J-------#
            mincard = floor[i][-1]
            if mincard[1] == "J":
                mincard = 10
                mincard = i + str(mincard)
            else:
                mincard = int(mincard[1:]) - 1
                mincard = i + str(mincard)
            #------------Add_Playable_Cards_To_The_List--------#
            list_of_playable_cards.append(mincard)
            list_of_playable_cards.append(maxcard)
            
            
    #---------check_for_playable_cards_in_player_hand-------#
    for i in list_of_playable_cards:
        if i in player['hand']:
            player['ava_moves'].append(i)

def play(player, floor, places):
    sort_cards_as_ref_list(floor)
    playable_cards(player, floor)
    if len(player["ava_moves"]) > 0:
        print_board(floor)
        print("player's hand: ", sorted(player['hand']))
        print("available cards to play: ", player["ava_moves"])
        while True:
            played_card = input("what card do you want to play?: ")
            if played_card in player["ava_moves"]:
                for i in ['s', 'd', 'h', 'c']:
                    if played_card[0] == i:
                        floor[i].append(player["hand"].pop(player["hand"].index(played_card)))
                        if len(player["hand"]) == 0:
                            player["place"] = places.pop(0)
                break
            else:
                print("invalid input")
    else:
        print("player has passed")


def play_bot(bot, floor, places):
    sort_cards_as_ref_list(floor)
    playable_cards(bot, floor)
    if len(bot["ava_moves"]) > 0:
        played_card = choice(bot["ava_moves"])
        for i in ['s', 'd', 'h', 'c']:
            if played_card[0] == i:
                floor[i].append(bot["hand"].pop(bot["hand"].index(played_card)))
                if len(bot["hand"]) == 0:
                    bot["place"] = places.pop(0)
        print(f"{bot['name']} played: ", played_card)
    else:
        print(f"{bot['name']} passed")
    

def reset_variables(player, bot_1, bot_2, bot_3):
    player['ava_moves'] = []
    bot_1['ava_moves'] = []
    bot_2['ava_moves'] = []
    bot_3['ava_moves'] = []