#This code uses pygame
def board_positions():
    """
    The purpose of this file is to establish the positions on the game board
    """
    ##Creating a simple list would be shorter, but copying and pasting for loops was easier
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
    listxend = [1227,1227,1298,1370,1440,1440,1440,1366] #manually appending the rest
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
    """

    Sets initial values of the board and piece positions

    """
    board_position, keys  = board_positions()
    pygame.init()
    width, height = int((1601*.7)), int((700*.7))
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\BoardLayout.png')
    reddot = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\reddot.png')
    bluedot = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\bluedot.png')
    board = pygame.transform.scale(background, [width,height])
    reddot = pygame.transform.scale(reddot, [40,40])
    bluedot = pygame.transform.scale(bluedot, [40, 40])
    screen.fill(0)
    screen.blit(board, [0, 0])
    screen.blit(reddot, board_position[1])
    screen.blit(bluedot,board_position[0])
    pygame.display.flip()
    input()
    return screen, width, height


def movement(index_initial, yell_leader, yellleader2, position_yell2):
    """
    Purpose: To display piece movement
    :param index_initial: The initial board pieces
    :param yell_leader: The first position piece
    :param yellleader2: The second position piece
    :param position_yell2: The location of second piece
    :return: Final position of first yell leader
    """
    background = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\BoardLayout.png')
    final_pos = index_initial
    width, height = int((1601 * .7)), int((700 * .7))
    board = pygame.transform.scale(background, [width, height])
    screen = pygame.display.set_mode((width, height))
    board_position = board_positions()[0]
    next_space = color_num_converter()[0]
    index = int(index_initial) + next_space
    final_pos =index
    screen.blit(yellleader2, board_position[position_yell2])
    for value in range(next_space):
        screen.blit(board)
        screen.blit(yell_leader, board_position[index_initial+value])
        pygame.display.flip()
    if index > 72:
        back = index - 72
        final_pos = index_initial - back
        for value in range(back):
            screen.blit(board)
            screen.blit(yell_leader, board_position[index_initial-back])
            pygame.display.flip()
    return final_pos
def rule_screen():
    """
    Code for the rule screen, they click to move to the next screen width
    """
    width, height = int((1601 * .7)), int((700 * .7))
    screen = pygame.display.set_mode((width, height))
    rules = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\MaroonBack.png')
    menuarrow = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Menu Arrow.png')
    menuarrow = pygame.transform.scale(menuarrow, [150, 85])
    enter = False
    while enter is False:
        screen.blit(rules, [0, 0])
        screen.blit(menuarrow, [800,400])
        pygame.display.flip()
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_position[0] > 800 and mouse_position[0] < 950 and mouse_position[1] > 400 and mouse_position[1] < 480:
                    init_game() #Based on where the user clicks the mouse, the rule screen will proceed to the first menu screen
                    enter = True
#rule_screen()
def Same_Spot(yellleader1, yellleader2, position):
    """
    parameters: The game pieces, and board position
    If both land on the same spot adjusts size so both are visible
    """
    init_game()
    yellleader1 = pygame.transform.scale(yellleader1,[20,20])  #shrinks the images
    yellleader2 = pygame.transform.scale(yellleader2,[20,20])
    width, height = int((1601 * .7)), int((700 * .7))
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\BoardLayout.png')
    board = pygame.transform.scale(background, [width, height])
    screen.blit(board,[0,0])
    screen.blit(yellleader1, position)
    screen.blit(yellleader2, [(position[0]+22), position[1]]) #Changes on of the positions
def random_color_generator(color_list):
    """

    :param color_list: The list of colors, preferably in order
    :return: Two Color Cards
    Purpose: To 'randomly' obtain two color card to be used for when player chooses between cards

    """
    import random as r
    color1= r.choice(color_list)
    color2 = r.choice(color_list) #using random.choose which chooses from a list 'randomly'
    return color1, color2
def color_num_converter(color,current_position):
    """
    Pupose: Converts the card colors to the actual locations on the board that pertain to them
    :param color: Card Color
    :param current_position: Position of the piece now
    :return: the final position to move to

    """
    blue = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Bluecard.png')
    pink = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Pinkcard.png')
    yellow = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Yellowcard.png')
    grey = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Greycard.png')
    Red = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\redcard.png')
    Green = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Greencard.png')
    color_list_str = ['blue', 'pink', 'yellow', 'grey', 'Red', 'Green']
    color_list = [blue, pink, yellow, grey, Red, Green]
    index_color = color_list.index(color)
    str_color = color_list_str[index_color]
def comp_num_generator():
    import random as r
    next_move = r.randint(0,6,)
    return next_move
print(comp_num_generator())
def card_choice_display():
    """

    Takes in player and returns card choice

    Purpose: Has the player choose their next card from one pre-set and one random card

    """
    pygame.init()
    width, height = int((1601 * .4)), int((700 * .5))
    card_screen = pygame.display.set_mode((width, height))
    player1_text = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Player1_words.png')
    player2_text = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Player1_words.png')
    blue = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Bluecard.png')
    pink = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Pinkcard.png')
    yellow = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Yellowcard.png')  #images to import
    grey = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Greycard.png')
    Red = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\redcard.png')
    Green = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Greencard.png')
    wood = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Wood.png')
    wood = pygame.transform.scale(wood, [width,height])
    randomcard = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Randomcard.png')
    end_turn = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\End_turn.png')
    end_turn = pygame.transform.scale(end_turn, [150,90])
    card_highlight = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Card_highlight.png')
    card_highlight = pygame.transform.scale(card_highlight, [155, 255])
    arrow_highlight = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [150,90])
    card_screen.blit(wood,[0,0])
    randomcard = pygame.transform.scale(randomcard, [140,240])
    cards = [blue, pink, yellow, grey, Red, Green]
    player1 = pygame.transform.scale(player1_text, [150, 45])
    player2 = pygame.transform.scale(player2_text, [150, 45])
    cards_new = []
    for item in cards:
        item = pygame.transform.scale(item, [155,255]) #Resizes each card
        cards_new.append(item)
    card_choice = 1
    color1 = random_color_generator(cards_new)[0]
    while card_choice == 1: #will keep screen up until choice is made
        card_screen.blit(randomcard, [50,75])
        card_screen.blit(color1, [250,75])
        card_screen.blit(player1, [10,40]) #Identifies player on screen
        pygame.display.flip()
        mouseposition = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: #if click is made
                if mouseposition[0] > 50 and mouseposition[0] < 200 and mouseposition[1] > 75 and mouseposition[1] < 325:
                    card_choice = 0
                    color2 = random_color_generator(cards_new)[1]
                    screen = True
                    while screen is True:  #If on random card, display the random card
                        card_screen.blit(color2, [50, 75])
                        card_screen.blit(player1, [10, 40])
                        card_screen.blit(end_turn, [425,250])
                        pygame.display.flip()
                        mouseposition = pygame.mouse.get_pos()
                        for event in pygame.event.get():
                            if  mouseposition[0] > 450 and mouseposition[0] < 600 and mouseposition[1] > 250 and mouseposition[1] < 340:
                                card_screen.blit(arrow_highlight, [425,250])
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if mouseposition[0] > 450 and mouseposition[0] < 600 and mouseposition[1] > 250 and mouseposition[1] < 340:
                                    screen = False  #Exits screen
                    return color2
                elif mouseposition[0] > 250 and mouseposition[0] < 400 and mouseposition[1] > 75 and mouseposition[1] < 325:
                    card_choice = 0 # if on known card, just exits
                    return color1
                    #Returns set card color
                else:
                    card_choice = 1
card_choice_display()
def menu1():
    """

    Purpose: Have the user decide two player or computer mode
    Executes the code for either

    """
    width, height = int((1601 * .7)), int((700 * .7))
    screen = pygame.display.set_mode((width, height))
    menu1 = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\MaroonBack.png')
    enter = False
    while enter is False:
        screen.blit(menu1, [0, 0])
        pygame.display.flip()
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_position[0] > 600 and mouse_position[0] < 1000) and (mouse_position[1] > 300 and mouse_position[1] < 400):
                    #Computer()
                    enter = True
                elif (mouse_position[0] > 200 and mouse_position[0] < 500) and (mouse_position[1] > 200 and mouse_position[1] < 299):
                    #Two_player()
                    enter = True
                else:
                    enter = False
def computer_mode(yellleader1, yellleader2):
    init_game()
    #position_com = 0
    #posiiton_player = 0
    #win = 0
    #while win == 0:
        #card_choice_display(color)
        #color_number_convertor() #Converts color to next position
        #movement
        #if win_check() = 1
            #Player 1 wins
            #display win screen
            #pygame.quit()
        #Computer movement
            #if win_check() = 2
            #display comp win screen
            #pygame.quit()
        # def computer_mode():
#def two_player(yellleader1, yellleader2):
    #init_game()
    #position_player1 = 0
    #posiiton_player2 = 0
    #win = 0
    #while win == 0:
        # card_choice_display(color, player)
        # color_number_convertor() #Converts color to next position
        # movement
        # if win_check() = 1
            # Player 1 wins
            # display win screen
            # pygame.quit()
        # player 2 card_choice(color, player)
        #color_number_convertor()
        #movement #displys movement
            # if win_check() = 1
            # display player2 win scree
            # pygame.quit()
