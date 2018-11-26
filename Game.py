
def board_positions():
    spacex=[]
    spacey = []
    start1 = 19
    for spaces in range(9):
        y = start1 + (spaces*77)
        spacey.append(y)
        spacex.append(22)
    start2x = spacex[-1]
    start2y = spacey[-1]
    for spaces2 in range(4):
        spacey.append(start2y)
        x = start2x + ((spaces2+1)*71)
        spacex.append(x)
    start3x = spacex[-1]
    start3y = spacey[-1]
    for spaces3 in range(7):
        y = (start3y+3) - ((spaces3+1) * 75)
        spacey.append(y)
        spacex.append(start3x)
    start4x = spacex[-1]
    start4y = spacey[-1]
    for spaces4 in range(3):
        spacey.append(start4y)
        x = start4x + ((spaces4+1)*72)
        spacex.append(x)
    start5x = spacex[-1]
    start5y = spacey[-1]
    for spaces5 in range(6):
        y = start5y + ((spaces5+1)*75)
        spacey.append(y)
        spacex.append(start5x)
    start6x = spacex[-1]
    start6y = spacey[-1]
    for spaces6 in range(3):
        spacey.append(start6y)
        x = start6x + ((spaces6 + 1) * 72)
        spacex.append(x)
    start7x = spacex[-1]
    start7y = spacey[-1]
    for spaces7 in range(7):
        y = (start7y-3) - ((spaces7+1) * 75)
        spacey.append(y)
        spacex.append(start7x)
    start8x = spacex[-1]
    start8y = spacey[-1]
    for spaces8 in range(3):
        spacey.append(start8y)
        x = (start8x-2) + ((spaces8 + 1) * 72)
        spacex.append(x)
    spacex.append(950)
    spacey.append(110)
    start9x = 1018
    start9y = spacey[-1]
    for spaces9 in range(8):
        y = start9y + ((spaces9) * 75)
        spacey.append(y)
        spacex.append(start9x)
    start10x = spacex[-1]
    start10y = spacey[-1]
    for spaces10 in range(7):
        spacey.append(start10y)
        x = (start10x-2) + ((spaces10 + 1) * 71)
        spacex.append(x)
    start11x = spacex[-1]
    start11y = spacey[-1]
    for spaces11 in range(3):
        y = (start11y+3) - ((spaces11 + 1) * 75)
        spacey.append(y)
        spacex.append(start11x)
    start12x = spacex[-1]
    start12y = spacey[-1]
    for spaces12 in range(4):
        spacey.append(start12y)
        x = (start12x - 2) - ((spaces12 + 1) * 71)
        spacex.append(x)
    listxend = [1227,1227,1298,1370,1440,1440,1440,1366]
    listyend = [342,266,226,226,226,190,117,117]
    spacey += listyend
    spacex += listxend
    board_position = []
    for ind in range(len(spacex)):
        x = spacex[ind] * .7
        y = spacey[ind] * .7
        positionind = [x,y]
        board_position.append(positionind)
    keys = []
    for number in range(len(board_position)):
        item = str(number)
        keys.append(item)
    return board_position, keys
board_positions()
import pygame
from pygame.locals import *
def init_game():
    board_position, keys  = board_positions()
    pygame.init()
    width, height = int((1601*.7)), int((700*.7))
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\BoardLayout.png')
    reddot = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\reddot.png')
    bluedot = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\bluedot.png')
    board_position = []
    reddot = pygame.transform.scale(reddot, [20,20])
    bluedot = pygame.transform.scale(bluedot, [20, 20])
    screen.fill(0)
    screen.blit(board, [0, 0])
    screen.blit(reddot, board_position[0])
    screen.blit(bluedot,board_position[0])
    pygame.display.flip()
init_game()
def random_number_generator():
    board_position, keys = board_positions()
    next_space = 5
    return next_space
def movement(index_initial, yell_leader):
    width, height = int((1601 * .7)), int((700 * .7))
    screen = pygame.display.set_mode((width, height))
    board_position = board_positions()[0]
    next_space = random_number_generator()
    index = int(index_initial) + next_space
    for value in range(next_space):
        screen.blit(yell_leader, board_position[index_initial+value])
        pygame.display.flip()
    ###if index_initial >  This is for the end of board
def two_player():
    