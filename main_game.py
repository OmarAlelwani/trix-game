from vars import *
from funcs import *
from db_fucns import *

shuffle_deck(deck)
dist_cards(deck, player, bot_1, bot_2, bot_3)

while game_is_running(player, bot_1, bot_2, bot_3):
    
    play(player, floor, places)
    play_bot(bot_1, floor, places)
    play_bot(bot_2, floor, places)
    play_bot(bot_3, floor, places)
    reset_variables(player, bot_1, bot_2, bot_3)

print_scores(player, bot_1, bot_2, bot_3)
#----------Database-Code---------#
create_database("Trix_Game")
#--------------------------------#
#create_table("Played_Games", "ID", "INTEGER PRIMARY KEY", "player", "text", "BOT_1", "text", "BOT_2", "text", "BOT_3", "text")
insert_values_to_a_table("Played_Games", ["player", "BOT_1", "BOT_2", "BOT_3"], player["place"], bot_1["place"], bot_2["place"], bot_3["place"])
