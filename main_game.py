from vars import *
from funcs import *

shuffle_deck(deck)
dist_cards(deck, player, bot_1, bot_2, bot_3)

while game_is_running(player, bot_1, bot_2, bot_3):
    
    play(player, floor, places)
    play_bot(bot_1, floor, places)
    play_bot(bot_2, floor, places)
    play_bot(bot_3, floor, places)
    reset_variables(player, bot_1, bot_2, bot_3)

print_scores(player, bot_1, bot_2, bot_3)

