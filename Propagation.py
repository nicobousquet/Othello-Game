def propagation(grid, direction, player_1, player_2, box_coord):
    #  fonction qui gère la propagation des cercles ou des croix
    #  grid: grille du jeu (array 2D)
    #  direction: North, South, West, East, North_West, North_East, South_West, South_East
    #  player_1: 'X' ou '0'
    #  player_2: 'X' ou '0'
    #  box_coord: coordonnées de la case jouée (tuple)
    #  return the number of boxes reversed
    counter = 0
    number_of_lines = grid.shape[0] - 1  # nombre de lignes dans la grille (sans la première de lettres)
    number_of_column = grid.shape[1] - 1  # nombre de colonnes dans la grille (sans la première de chiffres)
    current_line = box_coord[0]  # ligne de la case jouée
    current_column = box_coord[1]  # colonne de la case jouée
    number_of_boxes_reversed = 0
    if direction == 'North':  # on regarde pour la propagation vers le haut
        for i in range(1, current_line):  # on boucle sur le rayon vers le haut
            if grid[current_line - i, current_column] == player_2:  # si la case est une case de l'adversaire
                continue
            elif grid[current_line - i, current_column] == player_1:  # si la case est une case à soi
                counter = i
                number_of_boxes_reversed = counter-1
            break
        for j in range(1, counter):
            grid[current_line - j, current_column] = player_1  # on remplace la case adverse par une case à soi

    # même méthode pour toutes les autres directions ###################################################################
    if direction == 'South':
        for i in range(1, number_of_lines - current_line + 1):
            if grid[current_line + i, current_column] == player_2:
                continue
            elif grid[current_line + i, current_column] == player_1:
                counter = i
                number_of_boxes_reversed += counter-1
            break
        for j in range(1, counter):
            grid[current_line + j, current_column] = player_1

    if direction == 'West':
        for i in range(1, current_column):
            if grid[current_line, current_column - i] == player_2:
                continue
            elif grid[current_line, current_column - i] == player_1:
                counter = i
                number_of_boxes_reversed += counter-1
            break
        for j in range(1, counter):
            grid[current_line, current_column - j] = player_1

    if direction == 'East':
        for i in range(1, number_of_column - current_column + 1):
            if grid[current_line, current_column + i] == player_2:
                continue
            elif grid[current_line, current_column + i] == player_1:
                counter = i
                number_of_boxes_reversed += counter-1
            break
        for j in range(1, counter):
            grid[current_line, current_column + j] = player_1

    if direction == 'North_West':
        for i in range(1, min(current_line, current_column)):
            if grid[current_line - i, current_column - i] == player_2:
                continue
            elif grid[current_line - i, current_column - i] == player_1:
                counter = i
                number_of_boxes_reversed += counter-1
            break
        for j in range(1, counter):
            grid[current_line - j, current_column - j] = player_1

    if direction == 'North_East':
        for i in range(1, min(current_line, number_of_column - current_column + 1)):
            if grid[current_line - i, current_column + i] == player_2:
                continue
            elif grid[current_line - i, current_column + i] == player_1:
                counter = i
                number_of_boxes_reversed += counter-1
            break
        for j in range(1, counter):
            grid[current_line - j, current_column + j] = player_1

    if direction == 'South_West':
        for i in range(1, min(number_of_lines - current_line + 1, current_column)):
            if grid[current_line + i, current_column - i] == player_2:
                continue
            elif grid[current_line + i, current_column - i] == player_1:
                counter = i
                number_of_boxes_reversed += counter-1
            break
        for j in range(1, counter):
            grid[current_line + j, current_column - j] = player_1

    if direction == 'South_East':
        for i in range(1, min(number_of_lines - current_line + 1, number_of_column - current_column + 1)):
            if grid[current_line + i, current_column + i] == player_2:
                continue
            elif grid[current_line + i, current_column + i] == player_1:
                counter = i
                number_of_boxes_reversed += counter-1
            break
        for j in range(1, counter):
            grid[current_line + j, current_column + j] = player_1

    return number_of_boxes_reversed
