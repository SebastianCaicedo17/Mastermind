#Initialisation du jeu 
import random
#Variable Global qui est la liste des couleurs possibles. 
colors = ["Red", "Blue", "Green", "Orange", "Black", "White"]
#Fonction qui permet d'initiliser le jeux avec une liste de 6 couleurs et retroune une nouvelle liste avec 4 de ces couleurs

def init():
    random_colors = random.sample(colors, 4)
    return random_colors

##print(init())