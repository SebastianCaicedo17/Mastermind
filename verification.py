import initialisation
import player_turn

##game_list = initialisation.init()
##player_list = player_turn.player_turn()

def verification(game_list, player_list):
    good_colors = 0
    good_index = 0 
    if player_list == game_list: print("Vous avez gagner")
    else: 
        for current_number, current_color in enumerate(player_list):
            for current_game_number, current_game_color in enumerate(game_list):
                if current_color == current_game_color and current_number == current_game_number: 
                    good_colors += 1
                    good_index += 1
                elif current_color == current_game_color: 
                    good_colors += 1
    print("Vous avez", good_colors, "bonnnes couleurs")
    print(good_index, "sont bien placés")


##verification()






