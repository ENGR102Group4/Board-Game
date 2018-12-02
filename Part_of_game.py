from pygame import *
import random as rnd

# TODO: GRAPHICS IMPLEMENTATION WITH MENUS, AI, CHOICE BETWEEN KNOWN AND UNKNOWN CARD
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

def color_position(pos):
    if pos > 0 and pos != 15 and pos != 34 and pos != 52 and pos != 67 and pos < 71:
        if (pos - 1) % 6 == 0:
            return "pink"
        elif (pos - 2) % 6 == 0:
            return "blue"
        elif (pos - 3) % 6 == 0:
            return "yellow"
        elif (pos - 4) % 6 == 0:
            return "red"
        elif (pos - 5) % 6 == 0:
            return "purple"
        elif (pos - 6) % 6 == 0:
            return "green"
    elif pos == 0:
        return "start"
    elif pos == 15:
        return "sully"
    elif pos == 34:
        return "century"
    elif pos == 52:
        return "fish"
    elif pos == 67:
        return "quad"
    elif pos >= 71:
        return "kyle"
    else:
        return "error"


def color_card():
    card_num = int(71 * rnd.random())
    while card_num == 0:
        card_num = int(71 * rnd.random())
    if card_num != 15 and card_num != 34 and card_num != 52 and card_num != 67:
        double = rnd.choice([True] + [False] * 2)
    else:
        double = False
    return card_num, double


def card_to_space(pos, card, double):
    color_starting = color_position(pos)
    newpos = pos + 0
    if color_starting == "start":
        color_starting = "green"
    elif color_starting == "sully":
        color_starting = "yellow"
    elif color_starting == "quad":
        color_starting = "pink"
    elif color_starting == "century" or color_starting == "fish":
        color_starting = "red"

    if card == "sully":
        newpos = 15
    elif card == "century":
        newpos = 34
    elif card == "fish":
        newpos = 52
    elif card == "quad":
        newpos = 67

    elif color_starting == "pink" and pos <= 71:
        if card == "pink":
            newpos = pos + 6
        elif card == "blue":
            newpos = pos + 1
        elif card == "yellow":
            newpos = pos + 2
        elif card == "red":
            newpos = pos + 3
        elif card == "purple":
            newpos = pos + 4
        elif card == "green":
            newpos = pos + 5

    elif color_starting == "blue" and pos <= 71:
        if card == "pink":
            newpos = pos + 5
        if card == "blue":
            newpos = pos + 6
        if card == "yellow":
            newpos = pos + 1
        if card == "red":
            newpos = pos + 2
        if card == "purple":
            newpos = pos + 3
        if card == "green":
            newpos = pos + 4

    elif color_starting == "yellow" and pos <= 71:
        if card == "pink":
            newpos = pos + 4
        if card == "blue":
            newpos = pos + 5
        if card == "yellow":
            newpos = pos + 6
        if card == "red":
            newpos = pos + 1
        if card == "purple":
            newpos = pos + 2
        if card == "green":
            newpos = pos + 3

    elif color_starting == "red" and pos <= 71:
        if card == "pink":
            newpos = pos + 3
        if card == "blue":
            newpos = pos + 4
        if card == "yellow":
            newpos = pos + 5
        if card == "red":
            newpos = pos + 6
        if card == "purple":
            newpos = pos + 1
        if card == "green":
            newpos = pos + 2

    elif color_starting == "purple" and pos <= 71:
        if card == "pink":
            newpos = pos + 2
        if card == "blue":
            newpos = pos + 3
        if card == "yellow":
            newpos = pos + 4
        if card == "red":
            newpos = pos + 5
        if card == "purple":
            newpos = pos + 6
        if card == "green":
            newpos = pos + 1

    elif color_starting == ("green" or "start") and pos <= 71:
        if card == "pink":
            newpos = pos + 1
        if card == "blue":
            newpos = pos + 2
        if card == "yellow":
            newpos = pos + 3
        if card == 'red':
            newpos = pos + 4
        if card == 'purple':
            newpos = pos + 5
        if card == "green":
            newpos = pos + 6
    print(pos)
    print(newpos)
    try:
        if double:
            newpos += 6
        if newpos > 71:
            return pos
        else:
            return newpos
    except UnboundLocalError:
        return pos

def movement(index_initial, yell_leader, final_pos, yellleader2, position_yell2):
    """
    Purpose: To display piece movement
    :param index_initial: The initial board pieces
    :param yell_leader: The first position piece
    :param final_pos: The next_location
    :param yellleader2: The second position piece
    :param position_yell2: The location of second piece
    """
    background = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Board.png')
    width, height = int((1601 * .7)), int((700 * .7))
    board = pygame.transform.scale(background, [width, height])
    screen = pygame.display.set_mode((width, height))
    board_position = board_positions()[0]
    next_space = int(final_pos) - int(index_initial)
    for value in range(next_space+1):
        screen.blit(board, [0, 0])
        screen.blit(yellleader2, board_position[position_yell2])
        screen.blit(yell_leader, board_position[index_initial + value])
        pygame.display.flip()
    print('position: ', final_pos)
    print(type(final_pos))
    if final_pos == position_yell2:
       Same_Spot(yell_leader,yellleader2,final_pos)
    end_turn = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\End_turn.png')
    end_turn = pygame.transform.scale(end_turn, [150,80])
    arrow_highlight = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [160, 90])
    fin_turn = True
    highlight_position = [-300, 400]
    while fin_turn is True:
        screen.blit(end_turn, [850, 350])
        pygame.display.flip()
        for event in pygame.event.get():
            mouseposition = pygame.mouse.get_pos()
            screen.blit(arrow_highlight, highlight_position)
            pygame.display.flip()
            if mouseposition[0] > 840 and mouseposition[0] < 1000 and mouseposition[1] > 340 and mouseposition[1] < 440:
                highlight_position = [845, 345]
                pygame.display.flip()
            else:
                highlight_position = [-300,400]
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseposition[0] > 840 and mouseposition[0] < 1000 and mouseposition[1] > 340 and mouseposition[1] < 440:
                    fin_turn = False # Exits screen
def Same_Spot(yellleader1, yellleader2, position):
    """
    parameters: The game pieces, and board position
    :param position is a integer
    If both land on the same spot adjusts size so both are visible
    """
    print(type(position))
    yellleader1 = pygame.transform.scale(yellleader1,[30,30])  #shrinks the images
    yellleader2 = pygame.transform.scale(yellleader2,[30,30])
    board_position = board_positions()[0]
    width, height = int((1601 * .7)), int((700 * .7))
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Board.png')
    board = pygame.transform.scale(background, [width, height])
    screen.blit(board,[0,0])
    position_entity = board_position[position]
    screen.blit(yellleader1, position_entity)
    screen.blit(yellleader2, [position_entity[0] + 30, position_entity[0] +30]) #Changes on of the positions
    pygame.display.flip()
def init_game(icon1, icon2):
    """

    Sets initial values of the board and piece positions

    """
    board_position, keys  = board_positions()
    pygame.init()
    width, height = int((1601*.7)), int((700*.7))
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Board.png')
    board = pygame.transform.scale(background, [width,height])
    screen.fill(0)
    screen.blit(board, [0, 0])
    Same_Spot(icon1, icon2, 0)
    icon1 = pygame.transform.scale(icon1, [40,40])
    icon2 = pygame.transform.scale(icon2, [40, 40])
    pygame.display.flip()

def card_choice_display(card1, card2, player):
    pygame.init()
    width, height = int((1601 * .4)), int((700 * .5))
    card_screen = pygame.display.set_mode((width, height))
    player1_text = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Player1_words.png')
    player2_text = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Player1_words.png')
    blue = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Bluecard.png')
    pink = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Pinkcard.png')
    yellow = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Yellowcard.png')  # images to import
    Purple = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Violet.png')
    Red = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\redcard.png')
    Green = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Greencard.png')
    wood = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Wood.png')
    wood = pygame.transform.scale(wood, [width, height])
    randomcard = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Randomcard.png')
    end_turn = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\End_turn.png')
    end_turn = pygame.transform.scale(end_turn, [150, 90])
    card_highlight = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Card_highlight.png')
    card_highlight = pygame.transform.scale(card_highlight, [155, 255])
    arrow_highlight = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [150, 90])
    Sully =  pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Sully.png')
    Tree = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\tree.png')
    Fish_pond = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Fishpond.png')
    Quad = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Quad.png')
    card_screen.blit(wood, [0, 0])
    randomcard = pygame.transform.scale(randomcard, [140, 240])
    cards = [pink, blue, yellow, Red, Purple, Green, Sully, Tree, Fish_pond, Quad]
    names = ['pink', 'blue', 'yellow', 'red', 'purple', 'green', 'sully', 'century', 'fish', 'quad']
    if player == 'player 1':
        player1 = pygame.transform.scale(player1_text, [150, 45])
    else:
        player1 = pygame.transform.scale(player2_text, [150, 45])
    cards_new = []
    for item in cards:
        item = pygame.transform.scale(item, [155, 255])  # Resizes each card
        cards_new.append(item)
    card_choice = 1
    ind1 = names.index(card1)
    card1_image = cards_new[ind1]
    while card_choice == 1:  # will keep screen up until choice is made
        card_screen.blit(randomcard, [50, 75])
        card_screen.blit(card1_image, [250, 75])
        card_screen.blit(player1, [10, 40])  # Identifies player on screen
        pygame.display.flip()
        mouseposition = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  # if click is made
                if mouseposition[0] > 50 and mouseposition[0] < 200 and mouseposition[1] > 75 and mouseposition[
                    1] < 325:
                    card_choice = 0
                    ind2 = names.index(card2)
                    card2_image = cards_new[ind2]
                    screen = True
                    highlight_position = [-300, 400]
                    while screen is True:  # If on random card, display the random card
                        card_screen.blit(card2_image, [50, 75])
                        card_screen.blit(player1, [10, 40])
                        card_screen.blit(end_turn, [425, 250])
                        pygame.display.flip()
                        for event in pygame.event.get():
                            card_screen.blit(arrow_highlight, highlight_position)
                            mouseposition = pygame.mouse.get_pos()
                            pygame.display.flip()
                            if mouseposition[0] > 450 and mouseposition[0] < 600 and mouseposition[1] > 250 and mouseposition[1] < 340:
                                highlight_position = [425, 250]
                                pygame.display.flip()
                            else:
                                highlight_position = [-300,400]
                                pygame.display.flip()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if mouseposition[0] > 450 and mouseposition[0] < 600 and mouseposition[1] > 250 and mouseposition[1] < 340:
                                    screen = False  # Exits screen
                                    return card2, ind2
                elif mouseposition[0] > 250 and mouseposition[0] < 400 and mouseposition[1] > 75 and mouseposition[
                    1] < 325:
                    card_choice = 0  # if on known card, just exits
                    return card1, ind1
                    # Returns set card color
                else:
                    card_choice = 1


###### BASIC GAME - NO INTERFACE, AI, OR CHOICE BETWEEN KNOWN AND UNKNOWN CARD ######


#pos1 = 0
#pos2 = 0
#winner = False
#count = 0
#while not winner:
#    p1Card, p1Double = color_card()
#    p1Card = color_position(p1Card)
#    pos1 = card_to_space(pos1, p1Card, p1Double)
#    print("After drawing a", p1Card, "card, Player 1 position is", pos1, color_position(pos1))
#    p2Card, p2Double = color_card()
#    p2Card = color_position(p2Card)
#    pos2 = card_to_space(pos2, p2Card, p2Double)
#    print("After drawing a", p2Card, "card, Player 2 position is", pos2, color_position(pos2))
##    count += 1
 #   if pos1 == 71 or pos2 == 71:
 #       if pos1 == 71:
 #           print("Player 1 wins! The game ended in", count, "turns.")
 #       else:
 #           print("Player 2 wins! The game ended in", count, "turns.")
#winner = True

def computer_mode():
    Player1_icon = player_menu2()[0]
    Player1_icon = pygame.transform.scale(Player1_icon, [40, 40])
    computer_icon = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Computer_icon.png')
    computer_icon = pygame.transform.scale(computer_icon, [40, 40])
    init_game(Player1_icon, computer_icon)
    pos_initial = 0
    pos2_initial = 0
    winner = False
    count = 0
    while not winner:
        p1Card1, p1Double1 = color_card()
        p1Card2, p1Double2 = color_card()
        p1Card1 = color_position(p1Card1)
        p1Card2 = color_position(p1Card2)
        p1_card_fin = card_choice_display(p1Card1,p1Card2,'Player1')[0]
        if p1_card_fin == p1Card1:
            p1Double = p1Double1
        else:
            p1Double = p1Double2
        pos_final = card_to_space(pos_initial, p1_card_fin, p1Double)
        movement(pos_initial, Player1_icon, pos_final, computer_icon, pos2_initial)
        pos_initial = pos_final
        print("After drawing a", p1_card_fin, "card, Player 1 position is", pos_initial, color_position(pos_initial))
        p2Card, p2Double = color_card()
        p2Card = color_position(p2Card)
        pos2_final = card_to_space(pos2_initial, p2Card, p2Double)
        movement(pos2_initial, computer_icon, pos2_final, Player1_icon, pos_final)
        pos2_initial = pos2_final
        print("After drawing a", p2Card, "card, Player 2 position is", pos2_initial, color_position(pos2_initial))
        count += 1
        if pos_initial == 71 or pos2_initial == 71:
            if pos_initial == 71:
                print("Player 1 wins! The game ended in", count, "turns.")
            else:
                print("Player 2 wins! The game ended in", count, "turns.")
    winner = True
def player_menu2():
    """
    :return: Yell_leader icon and position of Yell Leader
    """
    width, height = int((1601 * .7)), int((700 * .7))
    screen = pygame.display.set_mode((width, height))
    Menu_2 = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\player 1 selection.png')
    selector = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Grey_highlight.png')
    selector = pygame.transform.scale(selector, [200, 260])
    Menu_2 = pygame.transform.scale(Menu_2, [width, height])
    Yell_1 = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Yell_1.png')
    Yell_2 = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Yell_2.png')
    Yell_3 = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Yell_3.png')
    Yell_4 = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Yell_4.png')
    Yell_5 = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Yell_5.png')
    enter = False
    position = [-400, 0]
    while enter is False:
        screen.blit(Menu_2, [0, 0])
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            screen.blit(selector, position)
            pygame.display.flip()
            if (mouse_position[0] > 20 and mouse_position[0] < 150) and (mouse_position[1] > 100 and mouse_position[1] < 400):
                position = [20, 130]
                pygame.display.flip()
            elif (mouse_position[0] > 260 and mouse_position[0] < 390) and (mouse_position[1] > 100 and mouse_position[1] < 400):
                position = [270, 130]
                pygame.display.flip()
            elif (mouse_position[0] > 500 and mouse_position[0] < 620) and (mouse_position[1] > 100 and mouse_position[1] < 400):
                position = [490, 130]
                pygame.display.flip()
            elif (mouse_position[0] > 730 and mouse_position[0] < 860) and (mouse_position[1] > 100 and mouse_position[1] < 400):
                position = [710, 130]
                pygame.display.flip()
            elif (mouse_position[0] > 930 and mouse_position[0] < 1100) and (mouse_position[1] > 100 and mouse_position[1] < 400):
                position = [930, 130]
                pygame.display.flip()
            else:
                position = [-400, 100]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_position[0] > 20 and mouse_position[0] < 150) and (mouse_position[1] > 100 and mouse_position[1] < 300):
                    return Yell_1, position
                elif (mouse_position[0] > 260 and mouse_position[0] < 390) and (mouse_position[1] > 100 and mouse_position[1] < 300):
                    return Yell_2, position
                elif (mouse_position[0] > 500 and mouse_position[0] < 620) and (mouse_position[1] > 100 and mouse_position[1] < 300):
                    return Yell_3, position
                elif (mouse_position[0] > 730 and mouse_position[0] < 860) and (mouse_position[1] > 100 and mouse_position[1] < 300):
                    return Yell_4, position
                elif (mouse_position[0] > 930 and mouse_position[0] < 1100) and (mouse_position[1] > 100 and mouse_position[1] < 300):
                    return Yell_5, position
def menu1():
    """

    Purpose: Have the user decide two player or computer mode
    Executes the code for either

    """
    width, height = int((1601 * .7)), int((700 * .7))
    screen = pygame.display.set_mode((width, height))
    menu1 = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\who will play.png')
    menu1 = pygame.transform.scale(menu1, [width, height])
    selector = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Grey_highlight.png')
    selector = pygame.transform.scale(selector, [350,350])
    enter = False
    position = [-400, 0]
    while enter is False:
        screen.blit(menu1, [0, 0])
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            screen.blit(selector, position)
            pygame.display.flip()
            if (mouse_position[0] > 100 and mouse_position[0] < 350) and (mouse_position[1] > 100 and mouse_position[1] < 450):
                position = [75, 120]
                pygame.display.flip()
            elif (mouse_position[0] > 700 and mouse_position[0] < 1050) and (mouse_position[1] > 100 and mouse_position[1] < 450):
                position = [720, 120]
                pygame.display.flip()
            else:
                position = [-400, 100]
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mouse_position[0] > 700 and mouse_position[0] < 1050) and (mouse_position[1] > 100 and mouse_position[1] < 450):
                    computer_mode()
                    enter = True
                elif (mouse_position[0] > 100 and mouse_position[0] < 350) and (mouse_position[1] > 100 and mouse_position[1] < 450):
                    #Two_player()
                    enter = True
                else:
                    enter = False
def rules():
    """
    Code for the rule screen, they click to move to the next screen width
    """
    width, height = int((1601 * .7)), int((700 * .7))
    screen = pygame.display.set_mode((width, height))
    rules = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\MaroonBack.png')
    menuarrow = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Menu Arrow.png')
    menuarrow = pygame.transform.scale(menuarrow, [150, 85])
    arrow_highlight = pygame.image.load('C:\\Users\\kayla\\Documents\\ENGR 102\\Final- Board Game\\Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [150, 90])
    enter = False
    while enter is False:
        screen.blit(rules, [0, 0])
        screen.blit(menuarrow, [800,400])
        position = [-800,400]
        pygame.display.flip()
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            screen.blit(arrow_highlight, position)
            pygame.display.flip()
            if (mouse_position[0] > 800 and mouse_position[0] < 950) and (mouse_position[1] > 390 and mouse_position[1] < 490):
                position = [800, 400]
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_position[0] > 800 and mouse_position[0] < 950 and mouse_position[1] > 400 and mouse_position[1] < 480:
                    menu1() #Based on where the user clicks the mouse, the rule screen will proceed to the first menu screen
                    enter = True
rules()