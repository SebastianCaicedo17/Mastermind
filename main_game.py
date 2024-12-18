import initialisation
import player_turn
import verification


print("Bienvenue dans le jeu du Mastermind")
print("Vous avec 10 essais")
print("Voici les couleurs disponibles")
print(initialisation.colors)

def main_game():
    game_list = initialisation.init()
    player_list = player_turn.player_turn()
    verification.verification(game_list, player_list)
    for game_turn in range (10):
        if game_turn == 9: print("Vous avez perdu")
        print("Tour n°", game_turn+1)
        verification.verification(game_list, player_list)
        player_turn.player_turn()


main_game ()


