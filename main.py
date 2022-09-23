import numpy as np
from random import randint
from Propagation import propagation
from Playable_boxes import playable_boxes

print("\n------------------------------                   Welcome                       ----------------------------\n")

#  on crée la grille ###################################################################################################

grid_size = int(input("Which size of grid do you want ? (<=26)\n"))

while grid_size > 26 or grid_size < 2:
    print("Grid size incorrect\n")
    grid_size = int(input("Which size of grid do you want ? (<=26)\n"))

mode = input("Which mode do you want to play ? \n - 1 vs 1 \n - 1 vs computer \n - computer vs computer \n")

Alphabet = {
    # on associe à chaque lettre le numéro de colonne
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

grid = np.zeros(shape=(grid_size + 1, grid_size + 1), dtype='object')
grid[:, :] = ['-']
grid[0, 1:] = [k for k in list(Alphabet.keys())[: grid_size]]  # on crée la première ligne de la grille
grid[1:, 0] = [str(k) for k in list(Alphabet.values())[: grid_size]]  # on crée la première colonne de la grille
player_1 = '0'  # le joueur 1 à les cercles
player_2 = 'X'  # le joueur 2 à les croix
grid[int(grid_size / 2), int(grid_size / 2)] = player_1
grid[int(grid_size / 2 + 1), int(grid_size / 2)] = player_2
grid[int(grid_size / 2), int(grid_size / 2 + 1)] = player_2
grid[int(grid_size / 2 + 1), int(grid_size / 2 + 1)] = player_1
print("\n" + str(grid) + "\n")  # on imprime la grille vide

########################################################################################################################

current_player = player_1  # la partie commence avec le joueur 1
opponent = player_2
while '-' in grid[1:, 1:]:  # tant qu'il reste des cases à remplir
    #  on vérifie qu'il y a des cases jouables pour le joueur
    #  si quand on joue une case, on retourne des pions adverses, alors, la case est jouable
    boxes = playable_boxes(grid, current_player, opponent, Alphabet)  # liste de toutes les cases jouables
    # pour current_player
    print("You can play : " + str(boxes) + "\n")

    if not boxes:  # si le joueur actuel ne peut pas jouer
        #  on vérifie que l'adversaire peut jouer
        boxes = playable_boxes(grid, opponent, current_player, Alphabet)  # liste de toutes les cases
        # jouables pour opponent
        if not boxes:  # si l'adversaire ne peut pas jouer non-plus, on arrête la partie
            print("None of the players can play, the party is over")
            break
        elif boxes:
            print(current_player + " doesn't have any legal box to play, you have to pass your turn")
            print(opponent + " this is your turn")
            current_player_copy = current_player
            current_player = opponent
            opponent = current_player_copy
            print("You can play : " + str(boxes) + "\n")

    if mode == "1 vs 1":
        box = input("Where do you want to play ?\n")  # le joueur choisit la case où il veut jouer
    elif mode == "1 vs computer":
        if current_player == '0':
            box = input("Where do you want to play ?\n")  # le joueur choisit la case où il veut jouer
        else:  # current_player == 'X':  # si l'ordinateur joue
            rand = randint(0, len(boxes) - 1)  # l'ordinateur joue au hasard une des cases jouables
            box = (boxes[rand])
    else:  # mode == "computer vs computer"
        rand = randint(0, len(boxes) - 1)  # l'ordinateur joue au hasard une des cases jouables
        box = (boxes[rand])

    current_column = Alphabet[box[0]]  # ligne de la case jouée
    current_line = int(box[1:])  # colonne de la case jouée
    box_coord = (current_line, current_column)  # coordonnées de la case jouée

    try:  # on vérifie que la case rentrée est valide
        grid[current_line, current_column]
    except Exception as e:
        print(e.__doc__)
        continue

    if grid[current_line, current_column] != '-':  # si la case n'est pas vide
        print("Box not empty")
        continue

    # on regarde la propagation du joueur dans toutes les directions
    number_of_boxes_reversed = (propagation(grid, 'North', current_player, opponent, box_coord) +
                                propagation(grid, 'South', current_player, opponent, box_coord) +
                                propagation(grid, 'West', current_player, opponent, box_coord) +
                                propagation(grid, 'East', current_player, opponent, box_coord) +
                                propagation(grid, 'North_West', current_player, opponent, box_coord) +
                                propagation(grid, 'North_East', current_player, opponent, box_coord) +
                                propagation(grid, 'South_West', current_player, opponent, box_coord) +
                                propagation(grid, 'South_East', current_player, opponent, box_coord))

    if number_of_boxes_reversed != 0:
        grid[current_line, current_column] = current_player  # on remplace la case par un cercle si des cases ont été
        print("\n" + str(grid) + "\n")  # on imprime la grille
        # retournées
    elif number_of_boxes_reversed == 0:
        print("Illegal box, retry !")
        continue
    current_player_copy = current_player
    current_player = opponent  # une fois que le joueur a joué, c'est au tour de l'autre joueur de jouer
    opponent = current_player_copy

number_of_X = np.count_nonzero(grid[1:, 1:] == 'X')
number_of_0 = np.count_nonzero(grid[1:, 1:] == '0')

print("Number of X: " + str(number_of_X))
print("Number of 0: " + str(number_of_0) + "\n")

if number_of_X > number_of_0:
    print("Winner is X")
elif number_of_0 > number_of_X:
    print("Winner is 0")
else:  # number_of_X == number_of_0
    print("Draw")  # match nul
