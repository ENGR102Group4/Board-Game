import random as rnd
import matplotlib.pyplot as plt
import statistics as stat

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


def computer_ai(pos, card, double):
    """
    Computer AI that determines the best move for the computer to make given the random option and known card
    :param pos: current position of player as integer
    :param card: known card as string
    :param double: whether known card is double as boolean
    :return: whether to accept known card or not as boolean
    """
    if pos <= 15 and card == 'sully':
        return False
    elif pos >= 33 and card == 'ring':
        return False
    elif pos >= 52 and card == 'fish':
        return False
    elif pos >= 66 and card == 'quad':
        return False
    elif double and ((pos >= 65 and card == 'purple') or (pos >= 64 and card == 'red') or (pos >= 63 and card ==
                     'yellow') or (pos >= 62 and card == 'blue') or (pos >= 61 and card == 'blue') or (pos >= 60 and
                     card == 'pink') or (pos >= 59 and card == 'green')):
        return False
    elif pos <= 60 and not double and card != 'sully' and card != 'ring' and card != 'fish' and card != 'quad':
        return False
    elif (card == 'green' and pos >= 66) or (card == 'pink' and pos >= 67) or (card == 'blue' and pos >= 68)\
            or (card == 'yellow' and pos >= 69) or (card == 'red' and pos >= 70):
            return False
    else:
        return True


def computer_ai_2(pos, card, double):
    """
    Computer AI that determines the best move for the computer to make given the random option and known card
    :param pos: current position of player as integer
    :param card: known card as string
    :param double: whether known card is double as boolean
    :return: whether to accept known card or not as boolean
    """
    if pos <= 15 and card == 'sully':
        return False
    elif pos >= 33 and card == 'ring':
        return False
    elif pos >= 52 and card == 'fish':
        return False
    elif pos >= 66 and card == 'quad':
        return False
    elif double and ((pos >= 65 and card == 'purple') or (pos >= 64 and card == 'red') or (pos >= 63 and card ==
                     'yellow') or (pos >= 62 and card == 'blue') or (pos >= 61 and card == 'blue') or (pos >= 60 and
                     card == 'pink') or (pos >= 59 and card == 'green')):
        return False
    elif pos <= 60 and not double and card != 'sully' and card != 'ring' and card != 'fish' and card != 'quad':
        return False
    elif (card == 'green' and pos >= 66) or (card == 'pink' and pos >= 67) or (card == 'blue' and pos >= 68)\
            or (card == 'yellow' and pos >= 69) or (card == 'red' and pos >= 70):
            return False
    else:
        return True


def computer_ai_random(pos, card, double):
    """
    Computer "AI" that returns random choices
    :param pos: unused, kept here for convenience of switching out functions
    :param card: unused, kept here for convenience of switching out functions
    :param double: unused, kept here for convenience of switching out functions
    :return: random boolean
    """
    return rnd.choice([True, False])


def computer_ai_dumb(pos, card, double):
    """
    Computer AI that determines the best move for the computer to make given the random option and known card
    :param pos: current position of player as integer
    :param card: known card as string
    :param double: whether known card is double as boolean
    :return: whether to accept known card or not as boolean
    """
    if card == 'sully':
        return True
    elif pos >= 33 and card == 'ring':
        return True
    elif pos >= 52 and card == 'fish':
        return True
    elif pos >= 66 and card == 'quad':
        return True
    elif pos <= 60 and not double and card != 'sully' and card != 'ring' and card != 'fish' and card != 'quad':
        return True
    elif (card == 'green' and pos >= 66) or (card == 'pink' and pos >= 67) or (card == 'blue' and pos >= 68)\
            or (card == 'yellow' and pos >= 69) or (card == 'red' and pos >= 70):
            return True
    else:
        return False


def computer_ai_dumb_2(pos, card, double):
    """
    Computer AI that determines the best move for the computer to make given the random option and known card
    :param pos: current position of player as integer
    :param card: known card as string
    :param double: whether known card is double as boolean
    :return: whether to accept known card or not as boolean
    """
    if pos <= 15 and card == 'sully':
        return True
    elif pos >= 33 and card == 'ring':
        return True
    elif pos >= 52 and card == 'fish':
        return True
    elif pos >= 66 and card == 'quad':
        return True
    elif double and ((pos >= 65 and card == 'purple') or (pos >= 64 and card == 'red') or (pos >= 63 and card ==
                     'yellow') or (pos >= 62 and card == 'blue') or (pos >= 61 and card == 'blue') or (pos >= 60 and
                     card == 'pink') or (pos >= 59 and card == 'green')):
        return True
    elif pos <= 60 and not double and card != 'sully' and card != 'ring' and card != 'fish' and card != 'quad':
        return True
    elif (card == 'green' and pos >= 66) or (card == 'pink' and pos >= 67) or (card == 'blue' and pos >= 68)\
            or (card == 'yellow' and pos >= 69) or (card == 'red' and pos >= 70):
            return True
    else:
        return False


def computer_v_computer():
    """
    Executes the game code by combining fundamental functions
    :return: nothing
    """
    c1_wins = 0
    c2_wins = 0
    total_games = 0
    for i in range(25000):
        pos_initial = 0
        pos2_initial = 0
        winner = False
        while not winner:
            c1_card, c1_double = color_card()
            c1_card = color_position(c1_card)
            if not computer_ai(pos_initial, c1_card, c1_double):
                c1_card, c1_double = color_card()
                c1_card = color_position(c1_card)
            pos_final = card_to_space(pos_initial, c1_card, c1_double)
            pos_initial = pos_final
            if pos_initial == 71:  # ends game play
                break
            c2_card, c2_double = color_card()
            c2_card = color_position(c2_card)
            if not computer_ai_2(pos2_initial, c2_card, c2_double):
                c2_card, c2_double = color_card()
                c2_card = color_position(c2_card)
            pos2_final = card_to_space(pos2_initial, c2_card, c2_double)
            pos2_initial = pos2_final
            if pos_initial == 71 or pos2_initial == 71:  # if a winner exists
                winner = True
        if pos_initial == 71:  # for computer player 1 winning
            c1_wins += 1
            total_games += 1
        else:  # for computer player 2 winning
            c2_wins += 1
            total_games += 1
    print("C1 (control) won", c1_wins, "times, or", c1_wins/total_games, "percent")
    print("C2 (experimental) won", c2_wins, "times, or", c2_wins / total_games, "percent")


def computer_v_computer_control():
    """
    Executes the game code by combining fundamental functions
    :return: nothing
    """
    c1_wins = 0
    c2_wins = 0
    total_games = 0
    countList = []
    for i in range(10000000):
        pos_initial = 0
        pos2_initial = 0
        count = 0
        winner = False
        while not winner:
            count += 1
            c1_card, c1_double = color_card()
            c1_card = color_position(c1_card)
            if not computer_ai(pos_initial, c1_card, c1_double):
                c1_card, c1_double = color_card()
                c1_card = color_position(c1_card)
            pos_final = card_to_space(pos_initial, c1_card, c1_double)
            pos_initial = pos_final
            if pos_initial == 71:  # ends game play
                break
            c2_card, c2_double = color_card()
            c2_card = color_position(c2_card)
            if not computer_ai(pos2_initial, c2_card, c2_double):
                c2_card, c2_double = color_card()
                c2_card = color_position(c2_card)
            pos2_final = card_to_space(pos2_initial, c2_card, c2_double)
            pos2_initial = pos2_final
            if pos_initial == 71 or pos2_initial == 71:  # if a winner exists
                winner = True
        if pos_initial == 71:  # for computer player 1 winning
            c1_wins += 1
            total_games += 1
            countList.append(count)
        else:  # for computer player 2 winning
            c2_wins += 1
            total_games += 1
            countList.append(count)
    print(max(countList), min(countList), sum(countList) / len(countList), stat.stdev(countList))
    print("C1 (control) won", c1_wins, "times, or", c1_wins/total_games, "percent")
    print("C2 (control) won", c2_wins, "times, or", c2_wins / total_games, "percent")
    plt.hist(countList, max(countList) - min(countList))
    plt.show()

#computer_v_computer()
computer_v_computer_control()
