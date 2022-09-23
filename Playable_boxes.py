from Propagation import propagation


def playable_boxes(grid, player_1, player_2, Alphabet):
    #  grid: grid of the game (2D array)
    #  player_1: 'X' or '0'
    #  player_2: 'X' or '0'
    #  Alphabet: dictionnary that associates each letter with a column
    #  retrun playable_boxes: list of all playable boxes for the current player
    boxes = []
    grid_size = len(grid)-1
    for j in list(Alphabet.values())[: grid_size]:
        for i in list(Alphabet.values())[: grid_size]:
            if grid[i, j] == '-':  # si la case est encore vide
                box_coord = (i, j)
                number_of_boxes_reversable = propagation(grid.copy(), 'North', player_1, player_2, box_coord)
                number_of_boxes_reversable += propagation(grid.copy(), 'South', player_1, player_2, box_coord)
                number_of_boxes_reversable += propagation(grid.copy(), 'West', player_1, player_2, box_coord)
                number_of_boxes_reversable += propagation(grid.copy(), 'East', player_1, player_2, box_coord)
                number_of_boxes_reversable += propagation(grid.copy(), 'North_West', player_1, player_2, box_coord)
                number_of_boxes_reversable += propagation(grid.copy(), 'North_East', player_1, player_2, box_coord)
                number_of_boxes_reversable += propagation(grid.copy(), 'South_West', player_1, player_2, box_coord)
                number_of_boxes_reversable += propagation(grid.copy(), 'South_East', player_1, player_2, box_coord)
                if number_of_boxes_reversable != 0:
                    boxes.append((list(Alphabet.keys())[j - 1] + str(i)))  # on crée la liste des cases
                    # jouables

    return boxes
