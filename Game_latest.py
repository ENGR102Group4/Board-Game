import pygame
import random as rnd


def board_positions():
    """
    establishes the positions on the game board
    """
    # creating a simple list would be shorter, but copying and pasting for loops was easier
    space_x = []
    space_y = []
    start1 = 19
    for spaces in range(9):
        y = start1 + (spaces*77)
        space_y.append(y)
        space_x.append(22)
    start2x = space_x[-1]
    start2y = space_y[-1]
    for spaces2 in range(4):
        space_y.append(start2y)
        x = start2x + ((spaces2+1)*71)
        space_x.append(x)
    start3x = space_x[-1]
    start3y = space_y[-1]
    for spaces3 in range(7):
        y = (start3y+3) - ((spaces3+1) * 75)
        space_y.append(y)
        space_x.append(start3x)
    start4x = space_x[-1]
    start4y = space_y[-1]
    for spaces4 in range(3):
        space_y.append(start4y)
        x = start4x + ((spaces4+1)*72)
        space_x.append(x)
    start5x = space_x[-1]
    start5y = space_y[-1]
    for spaces5 in range(6):
        y = start5y + ((spaces5+1)*75)
        space_y.append(y)
        space_x.append(start5x)
    start6x = space_x[-1]
    start6y = space_y[-1]
    for spaces6 in range(3):
        space_y.append(start6y)
        x = start6x + ((spaces6 + 1) * 72)
        space_x.append(x)
    start7x = space_x[-1]
    start7y = space_y[-1]
    for spaces7 in range(7):
        y = (start7y-3) - ((spaces7+1) * 75)
        space_y.append(y)
        space_x.append(start7x)
    start8x = space_x[-1]
    start8y = space_y[-1]
    for spaces8 in range(3):
        space_y.append(start8y)
        x = (start8x-2) + ((spaces8 + 1) * 72)
        space_x.append(x)
    space_x.append(950)
    space_y.append(110)
    start9x = 1018
    start9y = space_y[-1]
    for spaces9 in range(8):
        y = start9y + (spaces9 * 75)
        space_y.append(y)
        space_x.append(start9x)
    start10x = space_x[-1]
    start10y = space_y[-1]
    for spaces10 in range(7):
        space_y.append(start10y)
        x = (start10x-2) + ((spaces10 + 1) * 71)
        space_x.append(x)
    start11x = space_x[-1]
    start11y = space_y[-1]
    for spaces11 in range(3):
        y = (start11y+3) - ((spaces11 + 1) * 75)
        space_y.append(y)
        space_x.append(start11x)
    start12x = space_x[-1]
    start12y = space_y[-1]
    for spaces12 in range(4):
        space_y.append(start12y)
        x = (start12x - 2) - ((spaces12 + 1) * 71)
        space_x.append(x)
    list_x_end = [1227, 1227, 1298, 1370, 1440, 1440, 1440, 1366]  # manually appending the rest
    list_y_end = [342, 266, 266, 266, 266, 190, 117, 117]
    space_y += list_y_end
    space_x += list_x_end
    board_position = []
    for ind in range(len(space_x)):
        x = space_x[ind] * .7
        y = space_y[ind] * .7
        positionind = [x, y]
        board_position.append(positionind)
    keys = []
    for number in range(len(board_position)):
        item = str(number)
        keys.append(item)
    return board_position, keys


def color_position(pos):
    """
    Gives the correct color/identity of a square
    :param pos: Position of player as integer
    :return: Name of position as string
    """
    if pos > 0 and pos != 15 and pos != 34 and pos != 52 and pos != 67 and pos < 71:
        if (pos - 1) % 6 == 0:
            return 'pink'
        elif (pos - 2) % 6 == 0:
            return 'blue'
        elif (pos - 3) % 6 == 0:
            return 'yellow'
        elif (pos - 4) % 6 == 0:
            return 'red'
        elif (pos - 5) % 6 == 0:
            return 'purple'
        elif (pos - 6) % 6 == 0:
            return 'green'
    elif pos == 0:
        return 'start'
    elif pos == 15:
        return 'sully'
    elif pos == 34:
        return 'century'
    elif pos == 52:
        return 'fish'
    elif pos == 67:
        return 'quad'
    elif pos >= 71:
        return 'kyle'
    else:
        return 'error'


def color_card():
    """
    Draws a card
    :return: Card color as an integer and whether it is double
    """
    card_num = int(71 * rnd.random())
    while card_num == 0:
        card_num = int(71 * rnd.random())
    if card_num != 15 and card_num != 34 and card_num != 52 and card_num != 67:
        double = rnd.choice([True] + [False] * 2)
    else:
        double = False
    return card_num, double


def card_to_space(pos, card, double):
    """
    gives new space from original space and card
    :param pos: initial position of player as int
    :param card: drawn card as string
    :param double: whether drawn card is double
    :return: new position as integer
    """
    color_starting = color_position(pos)
    newpos = pos + 0
    if color_starting == 'start':
        color_starting = 'green'
    elif color_starting == 'sully':
        color_starting = 'yellow'
    elif color_starting == 'quad':
        color_starting = 'pink'
    elif color_starting == 'century' or color_starting == 'fish':
        color_starting = 'red'
    if card == 'sully':
        newpos = 15
    elif card == 'century':
        newpos = 34
    elif card == 'fish':
        newpos = 52
    elif card == 'quad':
        newpos = 67
    elif color_starting == 'pink' and pos <= 71:
        if card == 'pink':
            newpos = pos + 6
        elif card == 'blue':
            newpos = pos + 1
        elif card == 'yellow':
            newpos = pos + 2
        elif card == 'red':
            newpos = pos + 3
        elif card == 'purple':
            newpos = pos + 4
        elif card == 'green':
            newpos = pos + 5
    elif color_starting == 'blue' and pos <= 71:
        if card == 'pink':
            newpos = pos + 5
        if card == 'blue':
            newpos = pos + 6
        if card == 'yellow':
            newpos = pos + 1
        if card == 'red':
            newpos = pos + 2
        if card == 'purple':
            newpos = pos + 3
        if card == 'green':
            newpos = pos + 4
    elif color_starting == 'yellow' and pos <= 71:
        if card == 'pink':
            newpos = pos + 4
        if card == 'blue':
            newpos = pos + 5
        if card == 'yellow':
            newpos = pos + 6
        if card == 'red':
            newpos = pos + 1
        if card == 'purple':
            newpos = pos + 2
        if card == 'green':
            newpos = pos + 3
    elif color_starting == 'red' and pos <= 71:
        if card == 'pink':
            newpos = pos + 3
        if card == 'blue':
            newpos = pos + 4
        if card == 'yellow':
            newpos = pos + 5
        if card == 'red':
            newpos = pos + 6
        if card == 'purple':
            newpos = pos + 1
        if card == 'green':
            newpos = pos + 2
    elif color_starting == 'purple' and pos <= 71:
        if card == 'pink':
            newpos = pos + 2
        if card == 'blue':
            newpos = pos + 3
        if card == 'yellow':
            newpos = pos + 4
        if card == 'red':
            newpos = pos + 5
        if card == 'purple':
            newpos = pos + 6
        if card == 'green':
            newpos = pos + 1
    elif color_starting == ('green' or 'start') and pos <= 71:
        if card == 'pink':
            newpos = pos + 1
        if card == 'blue':
            newpos = pos + 2
        if card == 'yellow':
            newpos = pos + 3
        if card == 'red':
            newpos = pos + 4
        if card == 'purple':
            newpos = pos + 5
        if card == 'green':
            newpos = pos + 6
    try:
        if double:
            newpos += 6
        if newpos > 71:
            return pos
        else:
            return newpos
    except UnboundLocalError:
        return pos


def movement(index_initial, yell_leader, final_pos, yell_leader2, position_yell2, arrow):
    """
    To display piece movement
    :param index_initial: The initial board pieces
    :param yell_leader: The first position piece
    :param final_pos: The next_location
    :param yell_leader2: The second position piece
    :param position_yell2: The location of second piece
    :param arrow directs the user to the next players move
    """
    background = pygame.image.load('Board.png')
    width, height = 1120, 490  # changing size so fits better on screen
    board = pygame.transform.scale(background, [width, height])  # transform.scale changes the size of an image
    screen = pygame.display.set_mode((width, height))
    board_position = board_positions()[0]
    next_space = int(final_pos) - int(index_initial)  # the amount of spaces necessary to move
    if next_space > 0:  # if position progress
        for value in range(next_space+1):
            screen.blit(board, [0, 0])
            screen.blit(yell_leader2, board_position[position_yell2])
            screen.blit(yell_leader, board_position[index_initial + value])
            pygame.display.flip()  # necessary for images to appear
            if final_pos == position_yell2:
                same_spot(yell_leader, yell_leader2, final_pos)  # a function run it the two images are on the same game piece
    elif next_space < 0:  # for backward progress
        for value in range(-next_space + 1):
            screen.blit(board, [0, 0])
            screen.blit(yell_leader2, board_position[position_yell2])
            screen.blit(yell_leader, board_position[index_initial - value])
            if final_pos == position_yell2:
                same_spot(yell_leader, yell_leader2, final_pos)
    else:  # for no progress
        screen.blit(board, [0, 0])
        screen.blit(yell_leader2, board_position[position_yell2])
        screen.blit(yell_leader, board_position[index_initial])
        if final_pos == position_yell2:
            same_spot(yell_leader, yell_leader2, final_pos)
    arrow = pygame.transform.scale(arrow, [160, 80])
    arrow_highlight = pygame.image.load('Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [160, 90])
    fin_turn = True
    highlight_position = [-300, 400]
    while fin_turn is True:  # displays screen until user clicks arrow
        screen.blit(arrow, [852, 350])
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()  # obtains the mouse position
            screen.blit(arrow_highlight, highlight_position)
            pygame.display.flip()
            if 840 < mouse_pos[0] < 1000 and 340 < mouse_pos[1] < 440:
                highlight_position = [855, 345]  # highlights arrow for user
                pygame.display.flip()
            else:
                highlight_position = [-300, 400]
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:  # only if the mouse button is pressed down
                if 840 < mouse_pos[0] < 1000 and 340 < mouse_pos[1] < 440:
                    fin_turn = False  # exits screen
            if event.type == pygame.QUIT:  # allows to quit gracefully
                pygame.quit()
                exit(0)


def same_spot(yell_leader1, yell_leader2, position):
    """
    :param yell_leader1: The first position piece as an image
    :param yell_leader2: The second position piece as an image
    :param position as a integer
    If both land on the same spot, adjusts size so both are visible
    """
    yell_leader1 = pygame.transform.scale(yell_leader1, [30, 30])  # shrinks the images
    yell_leader2 = pygame.transform.scale(yell_leader2, [30, 30])
    board_position = board_positions()[0]
    width, height = 1120, 490
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('Board.png')
    board = pygame.transform.scale(background, [width, height])
    screen.blit(board, [0, 0])
    position_entity = board_position[position]
    screen.blit(yell_leader1, position_entity)
    screen.blit(yell_leader2, [(position_entity[0] + 20), (position_entity[1] + 20)])  # changes on of the positions


def init_game(icon1, icon2):
    """
    Sets initial values of the board and piece positions
    :param icon1 is the png image of player 1
    :param icon2  is the png image of player 2
    :return: nothing
    """
    pygame.init()
    width, height = 1120, 490
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('Board.png')
    board = pygame.transform.scale(background, [width, height])
    screen.fill(0)
    screen.blit(board, [0, 0])
    same_spot(icon1, icon2, 0)
    pygame.display.flip()
    arrow = pygame.image.load('Player1arrow.png')
    arrow = pygame.transform.scale(arrow, [160, 80])
    arrow_highlight = pygame.image.load('Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [160, 90])
    fin_turn = True
    highlight_position = [-300, 400]
    while fin_turn is True:  # displays screen until user clicks arrow
        screen.blit(arrow, [852, 350])
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()  # obtains the mouse position
            screen.blit(arrow_highlight, highlight_position)
            pygame.display.flip()
            if 840 < mouse_pos[0] < 1000 and 340 < mouse_pos[1] < 440:
                highlight_position = [855, 345]  # highlights arrow for user
                pygame.display.flip()
            else:
                highlight_position = [-300, 400]
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:  # only if the mouse button is pressed down
                if 840 < mouse_pos[0] < 1000 and 340 < mouse_pos[1] < 440:
                    fin_turn = False  # exits screen
            if event.type == pygame.QUIT:  # allows to quit gracefully
                pygame.quit()
                exit(0)


def card_choice_display(card1, double1, card2, double2, player):
    """
    Screen in which user chooses between a known card and an unknown card
    :param card1: The known card to choose from
    :param double1: whether the first card is a doubled card
    :param card2: The unknown card to choose from
    :param double2: whether the second card is a doubled card
    :param player: the players turn in order to display it
    :return: set card color
    """
    pygame.init()
    width, height = 640, 350  # smaller screen
    card_screen = pygame.display.set_mode((width, height))
    player1_text = pygame.image.load('Player1_words.png')
    player2_text = pygame.image.load('Player2_words.png')
    blue = pygame.image.load('Bluecard.png')
    pink = pygame.image.load('Pinkcard.png')
    yellow = pygame.image.load('Yellowcard.png')  # images to import
    purple = pygame.image.load('Violet.png')
    red = pygame.image.load('redcard.png')
    green = pygame.image.load('Greencard.png')
    wood = pygame.image.load('Wood.png')
    wood = pygame.transform.scale(wood, [width, height])  # changing size
    random_card = pygame.image.load('Randomcard.png')
    end_turn = pygame.image.load('End_turn.png')
    end_turn = pygame.transform.scale(end_turn, [150, 90])
    arrow_highlight = pygame.image.load('Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [150, 90])
    sully = pygame.image.load('Sully.png')
    tree = pygame.image.load('tree.png')
    fish_pond = pygame.image.load('Fishpond.png')
    quad = pygame.image.load('Quad.png')
    double = pygame.image.load('double.png')
    card_screen.blit(wood, [0, 0])
    random_card = pygame.transform.scale(random_card, [140, 240])
    cards = [pink, blue, yellow, red, purple, green, sully, tree, fish_pond, quad]  # list of possible cards
    names = ['pink', 'blue', 'yellow', 'red', 'purple', 'green', 'sully', 'century', 'fish', 'quad']  # strings to match the cards
    if player == 'player1':  # displays which player's turn
        player1 = pygame.transform.scale(player1_text, [150, 45])
    else:
        player1 = pygame.transform.scale(player2_text, [150, 45])
    cards_new = []
    for item in cards:
        item = pygame.transform.scale(item, [155, 255])  # resizes each card
        cards_new.append(item)
    card_choice = False
    ind1 = names.index(card1)
    card1_image = cards_new[ind1]
    while not card_choice:
        card_screen.blit(random_card, [50, 75])
        card_screen.blit(card1_image, [250, 75])
        if double1:
            card_screen.blit(double, [325, 90])
        card_screen.blit(player1, [10, 40])  # identifies player on screen
        pygame.display.flip()
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:  # if click is made
                if 50 < mouse_pos[0] < 200 and 75 < mouse_pos[1] < 325:
                    ind2 = names.index(card2)
                    card2_image = cards_new[ind2]
                    screen = True
                    highlight_position = [-300, 400]
                    while screen is True:  # if on random card, display the random card
                        card_screen.blit(card2_image, [50, 75])
                        if double2:
                            card_screen.blit(double, [130, 90])
                        card_screen.blit(player1, [10, 40])
                        card_screen.blit(end_turn, [425, 250])
                        pygame.display.flip()
                        for event2 in pygame.event.get():
                            mouse_pos = pygame.mouse.get_pos()
                            card_screen.blit(arrow_highlight, highlight_position)
                            pygame.display.flip()
                            if 450 < mouse_pos[0] < 600 and 250 < mouse_pos[1] < 340:
                                highlight_position = [425, 250]
                                pygame.display.flip()
                            else:
                                highlight_position = [-300, 400]
                                pygame.display.flip()
                            if event2.type == pygame.MOUSEBUTTONDOWN:
                                if 450 < mouse_pos[0] < 600 and 250 < mouse_pos[1] < 340:
                                    return card2, ind2
                elif 250 < mouse_pos[0] < 400 and 75 < mouse_pos[1] < 325:
                    return card1, ind1  # returns set card color
                if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                    pygame.quit()
                    exit(0)


def player_menu3(position_grey):
    """
    This code asks player 2 to choose a player piece different than player 1 and enforces that
    :param position_grey: list, giving coordinates of other icon to black so it is not choosen
    :return: Yell_leader icon
    """
    width, height = 1120, 490
    screen = pygame.display.set_mode((width, height))
    menu_3 = pygame.image.load('player 2 character.png')
    selector = pygame.image.load('Grey_highlight.png')
    selector = pygame.transform.scale(selector, [200, 260])  # in order to display the selection
    menu_3 = pygame.transform.scale(menu_3, [width, height])
    yell_1 = pygame.image.load('Yell_1.png')
    yell_2 = pygame.image.load('Yell_2.png')
    yell_3 = pygame.image.load('Yell_3.png')
    yell_4 = pygame.image.load('Yell_4.png')
    yell_5 = pygame.image.load('Yell_5.png')
    grey_box = pygame.image.load('greybox.png')
    grey_box = pygame.transform.scale(grey_box, [200, 260])
    warning = pygame.image.load('warning.png')
    warning = pygame.transform.scale(warning, [200, 100])
    enter = False
    position_w = [-400, 0]  # negative so it doesnt stay blitted
    position = [-400, 0]
    while not enter:
        screen.blit(menu_3, [4, -2])
        screen.blit(grey_box, position_grey)  # in order to display the player1 choice
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(warning, position_w)  # if tries to choose player 1
            screen.blit(selector, position)
            pygame.display.flip()
            if 20 < mouse_pos[0] < 150 and 100 < mouse_pos[1] < 400:
                position = [20, 130]
                pygame.display.flip()
            elif 260 < mouse_pos[0] < 390 and 100 < mouse_pos[1] < 400:
                position = [270, 130]
                pygame.display.flip()
            elif 500 < mouse_pos[0] < 620 and 100 < mouse_pos[1] < 400:
                position = [490, 130]
                pygame.display.flip()
            elif 730 < mouse_pos[0] < 860 and 100 < mouse_pos[1] < 400:
                position = [710, 130]
                pygame.display.flip()
            elif 930 < mouse_pos[0] < 1100 and 100 < mouse_pos[1] < 400:
                position = [930, 130]
                pygame.display.flip()
            else:
                position = [-400, 100]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 20 < mouse_pos[0] < 150 and 100 < mouse_pos[1] < 400:
                    position2 = [20, 130]
                    if position2 == position_grey:
                        position_w = [200, 500]  # if position is the same as player 1, gives warning
                    else:
                        return yell_1
                elif 260 < mouse_pos[0] < 390 and 100 < mouse_pos[1] < 400:
                    position2 = [270, 130]
                    if position2 == position_grey:
                        position_w = [200, 500]
                    else:
                        return yell_2
                elif 500 < mouse_pos[0] < 620 and 100 < mouse_pos[1] < 400:
                    position2 = [490, 130]
                    if position2 == position_grey:
                        position_w = [200, 500]
                    else:
                        return yell_3
                elif 730 < mouse_pos[0] < 860 and 100 < mouse_pos[1] < 400:
                    position2 = [710, 130]
                    if position2 == position_grey:
                        position_w = [200, 500]
                    else:
                        return yell_4
                elif 930 < mouse_pos[0] < 1100 and 100 < mouse_pos[1] < 400:
                    position2 = [930, 130]
                    if position2 == position_grey:
                        position_w = [200, 500]
                    else:
                        return yell_5
            if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                pygame.quit()
                exit(0)


def computer_ai(pos, card, double):
    """
    Computer AI that determines the best move for the computer to make given the random option and known card
    :param pos: current position of player as integer
    :param card: known card as string
    :param double: whether known card is double as boolean
    :return: whether to accept known card or not as boolean
    """
    if card == 'sully':
        return False
    elif pos >= 33 and card == 'ring':
        return False
    elif pos >= 52 and card == 'fish':
        return False
    elif pos >= 66 and card == 'quad':
        return False
    elif pos <= 60 and not double and card != 'sully' and card != 'ring' and card != 'fish' and card != 'quad':
        return False
    elif (card == 'green' and pos >= 66) or (card == 'pink' and pos >= 67) or (card == 'blue' and pos >= 68)\
            or (card == 'yellow' and pos >= 69) or (card == 'red' and pos >= 70):
            return False
    else:
        return True


def computer_mode():
    """
    Executes the game code by combining fundamental functions
    :return: nothing
    """
    player1_icon1 = player_menu2()[0]
    player1_icon = pygame.transform.scale(player1_icon1, [40, 40])
    computer_icon = pygame.image.load('Computer_icon.png')
    computer_icon = pygame.transform.scale(computer_icon, [40, 40])
    computer_arrow = pygame.image.load('Computer_arrow.png')
    player1_arrow = pygame.image.load('Player1arrow.png')
    init_game(player1_icon, computer_icon)
    pos_initial = 0
    pos2_initial = 0
    winner = False
    count = 0
    while not winner:
        p1_card1, p1_double1 = color_card()  # choose the card and the chance of it being double
        p1_card2, p1_double2 = color_card()
        p1_card1 = color_position(p1_card1)  # gives the card position
        p1_card2 = color_position(p1_card2)
        p1_card_fin = card_choice_display(p1_card1, p1_double1, p1_card2, p1_double2, 'player1')[0]  # lets user choose the card
        if p1_card_fin == p1_card1:
            p1_double = p1_double1
        else:
            p1_double = p1_double2
        pos_final = card_to_space(pos_initial, p1_card_fin, p1_double)
        movement(pos_initial, player1_icon, pos_final, computer_icon, pos2_initial, computer_arrow)  # moves the piece
        pos_initial = pos_final  # changes coordinates
        if pos_initial == 71:  # ends game play
            break
        p2_card, p2_double = color_card()  # same for computer except excludes choice display
        p2_card = color_position(p2_card)
        if not computer_ai(pos2_initial, p2_card, p2_double):
            p2_card, p2_double = color_card()
            p2_card = color_position(p2_card)
        pos2_final = card_to_space(pos2_initial, p2_card, p2_double)
        movement(pos2_initial, computer_icon, pos2_final, player1_icon, pos_final, player1_arrow)
        pos2_initial = pos2_final
        count += 1
        computer_icon = pygame.image.load('Computer_icon.png')
        computer_icon = pygame.transform.scale(computer_icon, [40, 40])
        if pos_initial == 71 or pos2_initial == 71:  # if a winner exists
            winner = True
    if pos_initial == 71:  # for player1
        pygame.init()
        width, height = 1120, 490
        player_wins = pygame.image.load('Player1_winner.png')
        player_wins = pygame.transform.scale(player_wins, [width, height])
        icon = pygame.transform.scale(player1_icon1, [200, 200])
        still = 0
        while still == 0:
            end_screen = pygame.display.set_mode((width, height))
            end_screen.blit(player_wins, [0, 0])
            end_screen.blit(icon, [200, 200])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                    pygame.quit()
                    exit(0)
    else:  # for computer winning
        pygame.init()
        width, height = 1120, 490
        computer_wins = pygame.image.load('Computer_winner.png')
        computer_wins = pygame.transform.scale(computer_wins, [width, height])
        icon = pygame.transform.scale(computer_icon, [200, 200])
        still = 0
        while still == 0:
            end_screen = pygame.display.set_mode((width, height))
            end_screen.blit(computer_wins, [0, 0])
            end_screen.blit(icon, [200, 200])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)


def two_player():
    """
    This code executes the game for two player mode. It is very similar to computer v player with a few differences
    :return: nothing
    """
    menu_response = player_menu2()
    player_icon1 = menu_response[0]
    player1_icon = pygame.transform.scale(player_icon1, [40, 40])
    grey_position = menu_response[1]
    player2_icon1 = player_menu3(grey_position)
    player2_icon = pygame.transform.scale(player2_icon1, [40, 40])
    player2_arrow = pygame.image.load('Player2arrow.png')
    player1_arrow = pygame.image.load('Player1arrow.png')
    init_game(player1_icon, player2_icon)
    pos1_initial = 0
    pos2_initial = 0
    winner = False
    count = 0
    while not winner:
        p1_card1, p1_double1 = color_card()
        p1_card2, p1_double2 = color_card()
        p1_card1 = color_position(p1_card1)
        p1_card2 = color_position(p1_card2)
        p1_card_fin = card_choice_display(p1_card1, p1_double1, p1_card2, p1_double2, 'player1')[0]
        if p1_card_fin == p1_card1:
            p1_double = p1_double1
        else:
            p1_double = p1_double2
        pos_final = card_to_space(pos1_initial, p1_card_fin, p1_double)
        movement(pos1_initial, player1_icon, pos_final, player2_icon, pos2_initial, player2_arrow)
        pos1_initial = pos_final
        if pos1_initial == 71 or pos2_initial == 71:  # ends game play
            break
        p2_card1, p2_double1 = color_card()
        p2_card2, p2_double2 = color_card()
        p2_card1 = color_position(p2_card1)
        p2_card2 = color_position(p2_card2)
        p2_card_fin = card_choice_display(p2_card1, p2_double1, p2_card2, p2_double2, 'player2')[0]
        if p2_card_fin == p2_card1:
            p2_double = p2_double1
        else:
            p2_double = p2_double2
        pos2_final = card_to_space(pos2_initial, p2_card_fin, p2_double)
        movement(pos2_initial, player2_icon, pos2_final, player1_icon, pos_final, player1_arrow)
        pos2_initial = pos2_final
        count += 1
        if pos1_initial == 71 or pos2_initial == 71:
            winner = True  # ends game play
    if pos1_initial == 71:  # displays screen if winner was player 1
        pygame.init()
        width, height = 1120, 490
        player_wins = pygame.image.load('Player1_winner.png')
        player_wins = pygame.transform.scale(player_wins, [width, height])
        icon = pygame.transform.scale(player_icon1, [200, 200])
        still = 0
        while still == 0:  # keeps screen blitted until the red x is marked
            end_screen = pygame.display.set_mode((width, height))
            end_screen.blit(player_wins, [0, 0])
            end_screen.blit(icon, [200, 200])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                    pygame.quit()
                    exit(0)
    else:  # displays win screen if winner was player 2
        pygame.init()
        width, height = 1120, 490
        player2_wins = pygame.image.load('Player2_winner.png')
        player2_wins = pygame.transform.scale(player2_wins, [width, height])
        icon = pygame.transform.scale(player2_icon1, [200, 200])
        still = 0
        while still == 0:
            end_screen = pygame.display.set_mode((width, height))
            end_screen.blit(player2_wins, [0, 0])
            end_screen.blit(icon, [200, 200])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                    pygame.quit()
                    exit(0)


def player_menu2():
    """
    Purpose: Allows player 1 to choose their position piece
    :return: Yell_leader icon and position of Yell Leader
    """
    width, height = 1120, 490
    screen = pygame.display.set_mode((width, height))
    menu_2 = pygame.image.load('player 1 selection.png')  # background image for menu
    selector = pygame.image.load('Grey_highlight.png')
    selector = pygame.transform.scale(selector, [200, 260])
    menu_2 = pygame.transform.scale(menu_2, [width, height])  # image being resized
    yell_1 = pygame.image.load('Yell_1.png')
    yell_2 = pygame.image.load('Yell_2.png')
    yell_3 = pygame.image.load('Yell_3.png')
    yell_4 = pygame.image.load('Yell_4.png')
    yell_5 = pygame.image.load('Yell_5.png')
    enter = False
    position = [-400, 0]  # so that the selector is only blitted when hovering over yell leader
    while not enter:
        screen.blit(menu_2, [0, 0])
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()  # gets the position of the mouse
            screen.blit(selector, position)
            pygame.display.flip()
            if 20 < mouse_pos[0] < 150 and 100 < mouse_pos[1] < 400:
                position = [20, 130]
                pygame.display.flip()
            elif 260 < mouse_pos[0] < 390 and 100 < mouse_pos[1] < 400:
                position = [270, 130]
                pygame.display.flip()
            elif 500 < mouse_pos[0] < 620 and 100 < mouse_pos[1] < 400:
                position = [490, 130]
                pygame.display.flip()
            elif 730 < mouse_pos[0] < 860 and 100 < mouse_pos[1] < 400:
                position = [710, 130]
                pygame.display.flip()
            elif 930 < mouse_pos[0] < 1100 and 100 < mouse_pos[1] < 400:
                position = [930, 130]
                pygame.display.flip()
            else:
                position = [-400, 100]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 20 < mouse_pos[0] < 150 and 100 < mouse_pos[1] < 400:
                    return yell_1, position
                elif 260 < mouse_pos[0] < 390 and 100 < mouse_pos[1] < 400:
                    return yell_2, position
                elif 500 < mouse_pos[0] < 620 and 100 < mouse_pos[1] < 400:
                    return yell_3, position
                elif 730 < mouse_pos[0] < 860 and 100 < mouse_pos[1] < 400:
                    return yell_4, position
                elif 930 < mouse_pos[0] < 1100 and 100 < mouse_pos[1] < 400:
                    return yell_5, position  # returns position so it is known for player 2 to choose
            if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                pygame.quit()
                exit(0)


def menu1():
    """
    Purpose: Have the user decide two player or computer mode
    Executes the code for either
    """
    width, height = 1120, 490
    screen = pygame.display.set_mode((width, height))
    menu1_image = pygame.image.load('who will play.png')
    menu1_image = pygame.transform.scale(menu1_image, [width, height])
    selector = pygame.image.load('Grey_highlight.png')
    selector = pygame.transform.scale(selector, [350, 350])
    enter = False
    position = [-400, 0]
    while not enter:
        screen.blit(menu1_image, [0, 0])
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(selector, position)
            pygame.display.flip()
            if 100 < mouse_pos[0] < 350 and 100 < mouse_pos[1] < 450:
                position = [75, 120]
                pygame.display.flip()
            elif 700 < mouse_pos[0] < 1050 and 100 < mouse_pos[1] < 450:
                position = [720, 120]
                pygame.display.flip()
            else:
                position = [-400, 100]
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 700 < mouse_pos[0] < 1050 and 100 < mouse_pos[1] < 450:
                    computer_mode()
                    enter = True
                elif 100 < mouse_pos[0] < 350 and 100 < mouse_pos[1] < 450:
                    two_player()
                    enter = True
                else:
                    enter = False
            if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                pygame.quit()
                exit(0)


def rules():
    """
    Code for the rule screen, they click to move to the next screen width
    """
    width, height = 1120, 490
    screen = pygame.display.set_mode((width, height))
    rules_img = pygame.image.load('How to play.png')
    menu_arrow = pygame.image.load('Menu Arrow.png')
    menu_arrow = pygame.transform.scale(menu_arrow, [150, 85])
    arrow_highlight = pygame.image.load('Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [150, 90])
    enter = False
    while not enter:
        screen.blit(rules_img, [0, 0])
        screen.blit(menu_arrow, [800, 400])
        position = [-800, 400]
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(arrow_highlight, position)
            pygame.display.flip()
            if 800 < mouse_pos[0] < 950 and 390 < mouse_pos[1] < 490:
                position = [800, 400]
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 800 < mouse_pos[0] < 950 and 400 < mouse_pos[1] < 480:
                    menu1()  # Based on where user clicks, will proceed to the first menu screen
                    enter = True
            if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                pygame.quit()
                exit(0)


def welcome():
    """
    Code for the rule screen, they click to move to the next screen width
    """
    board_positions()
    width, height = 1120, 490
    screen = pygame.display.set_mode((width, height))
    welcome_screen = pygame.image.load('Welcome.png')
    welcome_screen = pygame.transform.scale(welcome_screen, [width, height])
    rule_arrow = pygame.image.load('Rule_arrow.png')
    rule_arrow = pygame.transform.scale(rule_arrow, [150, 85])
    arrow_highlight = pygame.image.load('Arrowhighlight.png')
    arrow_highlight = pygame.transform.scale(arrow_highlight, [150, 90])
    enter = False
    while not enter:
        screen.blit(welcome_screen, [0, 0])
        screen.blit(rule_arrow, [800, 400])
        position = [-800, 400]
        pygame.display.flip()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(arrow_highlight, position)
            pygame.display.flip()
            if 800 < mouse_pos[0] < 950 and 390 < mouse_pos[1] < 490:
                position = [800, 400]
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 800 < mouse_pos[0] < 950 and 400 < mouse_pos[1] < 480:
                    rules()  # Based on where user clicks, will proceed to the first menu screen
                    enter = True
            if event.type == pygame.QUIT:  # allows user to exit gracefully by hitting the red x
                pygame.quit()
                exit(0)


welcome()
