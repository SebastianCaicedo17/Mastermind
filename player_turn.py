import initialisation

#Fonction qui demande la proposition du joueur
#Pour cela je déclare une liste vide puis j'ajoute un input de l'utilisateur à chaque tour dans la liste global des couleurs

def player_turn ():
    player_list = []
    good_color = True

    for input_player in initialisation.colors[:4]:
        proposition_player = input("Entrez 1 couleur ")
        if proposition_player in initialisation.colors:
            player_list.append(proposition_player)     
        else:    
            print(f"{proposition_player} n'est pas une couleur valide recommencez.\n")
            proposition_player = input("Entrez une autre couleur ") 
            while proposition_player not in initialisation.colors:
                proposition_player = input("Entrez une autre couleur ")
            player_list.append(proposition_player)
    print("Voici votre proposition",player_list)
    return player_list

##print(initialisation.colors)
##player_turn()