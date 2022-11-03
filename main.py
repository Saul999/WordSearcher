import random
import string

from pprint import pprint

words = ['horn', 'honk', 'leet', 'stinky']

grid_size = 20

grid = [ [ '_' for _ in range(grid_size)] for _ in range(grid_size)]

def printGrid():
    for i in range(grid_size):
        print('\t'*5 + ' '.join(grid[i]))

orientations = [ 'updown', 'leftright', 'diagup', 'diagdown']

for word in words:
    wordlen = len(word)


    placed = False
    while not placed:
        orientation = random.choice(orientations)

        if orientation == 'updown':
            step_x = 0
            step_y = 1
        elif orientation == 'diagup':
            step_x = 1
            step_y = -1
        elif orientation == 'leftright':
            step_x = 1
            step_y = 0
        elif orientation == 'diagdown':
            step_x = 1
            step_y = 1

        x_pos = random.randint(0, grid_size)
        y_pos = random.randint(0, grid_size)

        end_x = x_pos + wordlen * step_x
        end_y = y_pos + wordlen * step_y

        if end_x < 0 or end_x >+ grid_size: continue
        if end_y < 0 or end_y >+ grid_size: continue

        failed = False

        for i in range (wordlen):
            character = word[i]
            
            new_position_x = x_pos+ i*step_x
            new_posiiton_y = y_pos+ i*step_y

            character_at_new_position = grid[new_position_x][new_posiiton_y]

            if character_at_new_position != '_':
                if character_at_new_position == character:
                    continue
                else:  
                    failed = True
                    break
        if failed:
            continue
        else:
            for i in range(wordlen):
                character  = word[i]

                new_posiiton_y = y_pos + i *step_y
                new_posiiton_x = x_pos + i *step_x

                grid[new_posiiton_x][new_posiiton_y] = character

            placed = True


for x in range(grid_size):
    for y in range(grid_size):
        if (grid[x][y] == '_'):
            grid[x][y] = random.choice(string.ascii_letters.upper())

printGrid()